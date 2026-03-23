"""
LangChain-powered agent for Quantum assistant.

Used as the intelligent fallback when the elif command chain doesn't match.
Provides:
  - Conversation memory   — last 8 exchanges, so follow-up questions work
  - Tool calling          — LLM routes to Python functions instead of guessing
  - Graceful degradation  — if packages/keys missing, returns None silently

Architecture
------------
    respond() elif chain  →  no match  →  run(voice_data)
                                               ↓ success
                                           reply(response)
                                               ↓ None (unavailable)
                                           random static fallback (unchanged)

Uses the modern LangChain LCEL API (compatible with langchain>=1.0):
  - InMemoryChatMessageHistory for session memory
  - llm.bind_tools()  for tool declaration
  - Manual tool-execution loop (no deprecated AgentExecutor)
"""

import os
import platform

_IS_MAC = platform.system() == 'Darwin'

# ---------------------------------------------------------------------------
# Session memory  (populated lazily)
# ---------------------------------------------------------------------------
_chat_history = None   # InMemoryChatMessageHistory
_llm_with_tools = None
_tool_map: dict = {}
_build_attempted = False


# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------

def _make_tools():
    """Return list of LangChain @tool functions and a name→callable map."""
    from langchain_core.tools import tool
    import re as _re

    @tool
    def search_web(query: str) -> str:
        """Search the web for a query and open the results in the browser."""
        import webbrowser
        webbrowser.get().open(f'https://google.com/search?q={query}')
        return f"Opened web search for '{query}'"

    @tool
    def open_application(app_name: str) -> str:
        """Open a macOS or Windows application by name (e.g. 'Calculator', 'Safari')."""
        import subprocess
        if _IS_MAC:
            r = subprocess.run(['open', '-a', app_name], capture_output=True, text=True)
            if r.returncode == 0:
                return f"Opened {app_name}"
            r2 = subprocess.run(['open', app_name], capture_output=True, text=True)
            return f"Opened {app_name}" if r2.returncode == 0 else f"Could not find '{app_name}'"
        else:
            try:
                os.startfile(app_name)
                return f"Opened {app_name}"
            except Exception as e:
                return f"Could not open '{app_name}': {e}"

    @tool
    def search_files(query: str) -> str:
        """Search for files and folders by name on this computer."""
        try:
            from quantum.file_search import search_files as _sf
            results = _sf(query)
            if not results:
                return f"No files found matching '{query}'"
            lines = [
                f"{i}. {'Folder' if is_dir else 'File'}: {os.path.basename(path)}"
                for i, (_, path, is_dir) in enumerate(results[:5], 1)
            ]
            return "Found:\n" + "\n".join(lines)
        except Exception as e:
            return f"File search failed: {e}"

    @tool
    def get_weather(city: str) -> str:
        """Get the current weather conditions for a city."""
        import requests as _req
        try:
            resp = _req.get(f'https://wttr.in/{city}?format=3', timeout=5)
            return resp.text.strip()
        except Exception as e:
            return f"Could not fetch weather for {city}: {e}"

    @tool
    def calculate(expression: str) -> str:
        """Evaluate a mathematical expression such as '25 * 48' or '100 / 4'."""
        try:
            safe = _re.sub(r'[^\d\+\-\*\/\.\(\)\s\%\*\*]', '', expression)
            if not safe.strip():
                return "Could not parse expression"
            result = eval(safe, {"__builtins__": {}})
            return f"{expression} = {result}"
        except Exception as e:
            return f"Could not calculate '{expression}': {e}"

    @tool
    def control_volume(action: str) -> str:
        """Control system volume. action must be 'up', 'down', 'mute', or 'unmute'."""
        import subprocess
        action = action.lower().strip()
        if _IS_MAC:
            scripts = {
                'up':     'set volume output volume (output volume of (get volume settings) + 10)',
                'down':   'set volume output volume (output volume of (get volume settings) - 10)',
                'mute':   'set volume output muted true',
                'unmute': 'set volume output muted false',
            }
            script = scripts.get(action)
            if script:
                subprocess.run(['osascript', '-e', script])
                return f"Volume {action}"
        else:
            import pyautogui
            key_map = {'up': 'volumeup', 'down': 'volumedown', 'mute': 'volumemute'}
            if action in key_map:
                pyautogui.press(key_map[action])
        return f"Volume {action}"

    @tool
    def take_screenshot() -> str:
        """Take a screenshot of the current screen and save it to the Desktop."""
        import pyautogui, datetime
        ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        path = os.path.expanduser(f'~/Desktop/screenshot_{ts}.png')
        pyautogui.screenshot(path)
        return f"Screenshot saved to {path}"

    @tool
    def get_datetime() -> str:
        """Get the current date and time."""
        import datetime
        now = datetime.datetime.now()
        return now.strftime("Today is %A, %B %d %Y. The time is %I:%M %p.")

    @tool
    def wikipedia_search(query: str) -> str:
        """Search Wikipedia for a 2-sentence summary about a topic."""
        try:
            import wikipedia
            return wikipedia.summary(query, sentences=2)
        except Exception as e:
            return f"Wikipedia search failed: {e}"

    tools = [
        search_web, open_application, search_files, get_weather,
        calculate, control_volume, take_screenshot, get_datetime,
        wikipedia_search,
    ]
    tool_map = {t.name: t for t in tools}
    return tools, tool_map


# ---------------------------------------------------------------------------
# LLM selection
# ---------------------------------------------------------------------------

_SYSTEM_PROMPT = (
    "You are Quantum, a helpful desktop AI assistant running on macOS. "
    "You have tools to search the web, open apps, find files, check weather, "
    "do math, control volume, take screenshots, get Wikipedia info, and get the time. "
    "Use a tool when the user wants to DO something on their computer or needs real-time data. "
    "For general knowledge or conversational questions, answer directly — no tool needed. "
    "Keep responses short and direct. One or two sentences unless more detail is truly needed."
)


def _get_llm():
    """Return best available LangChain LLM, or None."""
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

    gemini_key = os.getenv('GEMINI_API_KEY', '')
    if gemini_key:
        try:
            from langchain_google_genai import ChatGoogleGenerativeAI
            return ChatGoogleGenerativeAI(
                model='gemini-2.5-flash',
                google_api_key=gemini_key,
                temperature=0.3,
            )
        except Exception as e:
            print(f"[LangChain] Gemini unavailable: {e}")

    groq_key = os.getenv('GROQ_API_KEY', '')
    if groq_key:
        try:
            from langchain_groq import ChatGroq
            return ChatGroq(
                model='llama-3.3-70b-versatile',
                groq_api_key=groq_key,
                temperature=0.3,
            )
        except Exception as e:
            print(f"[LangChain] Groq unavailable: {e}")

    return None


# ---------------------------------------------------------------------------
# Agent construction
# ---------------------------------------------------------------------------

def _build_agent() -> bool:
    global _chat_history, _llm_with_tools, _tool_map

    llm = _get_llm()
    if llm is None:
        print("[LangChain] No LLM available — agent disabled.")
        return False

    try:
        from langchain_core.chat_history import InMemoryChatMessageHistory

        tools, tool_map_local = _make_tools()
        _llm_with_tools = llm.bind_tools(tools)
        _tool_map = tool_map_local
        _chat_history = InMemoryChatMessageHistory()
        print(f"[LangChain] Agent ready — {len(tools)} tools, memory enabled.")
        return True
    except Exception as e:
        print(f"[LangChain] Build failed: {e}")
        return False


# ---------------------------------------------------------------------------
# Agent execution loop
# ---------------------------------------------------------------------------

def run(user_input: str, max_iterations: int = 3) -> str | None:
    """
    Run the LangChain agent on *user_input*.
    Returns response string, or None if agent unavailable/errors.
    """
    global _build_attempted

    if _llm_with_tools is None:
        if _build_attempted:
            return None
        _build_attempted = True
        if not _build_agent():
            return None

    try:
        from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage

        # Build message list: system + history (last 16 msgs = 8 turns) + new input
        history_msgs = _chat_history.messages[-16:]
        messages = [SystemMessage(content=_SYSTEM_PROMPT)] + history_msgs + [HumanMessage(content=user_input)]

        # Agentic loop: call LLM → execute any tool calls → repeat
        for _ in range(max_iterations):
            response = _llm_with_tools.invoke(messages)
            messages.append(response)

            if not getattr(response, 'tool_calls', None):
                break   # no tools needed, we have the final answer

            # Execute each tool call and append results
            for tc in response.tool_calls:
                tool_fn = _tool_map.get(tc['name'])
                if tool_fn:
                    try:
                        result = tool_fn.invoke(tc['args'])
                    except Exception as te:
                        result = f"Tool error: {te}"
                else:
                    result = f"Unknown tool: {tc['name']}"
                messages.append(ToolMessage(content=str(result), tool_call_id=tc['id']))

        # Persist the exchange to history
        final_text = (response.content or "").strip()
        _chat_history.add_user_message(user_input)
        _chat_history.add_ai_message(final_text)

        return final_text if final_text else None

    except Exception as e:
        print(f"[LangChain] Agent error: {e}")
        return None


# ---------------------------------------------------------------------------
# Public memory utilities
# ---------------------------------------------------------------------------

def get_memory_summary() -> list:
    """Return conversation as [(role, preview), ...], oldest first."""
    if _chat_history is None:
        return []
    out = []
    for m in _chat_history.messages[-16:]:
        role = "You" if m.type == "human" else "Quantum"
        preview = m.content[:80] + ("…" if len(m.content) > 80 else "")
        out.append((role, preview))
    return out


def clear_memory() -> None:
    """Wipe all conversation memory."""
    if _chat_history is not None:
        _chat_history.clear()
