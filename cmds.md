# 🎯 Quantum Voice Commands – Extracted Command Reference

> After renaming Quantum, use the new name for all commands.
> Example: `quantum change name to jarvis` → `jarvis hello`

---

# 🔧 1. Basic Commands

- quantum hello
- quantum what is your name
- quantum who are you
- quantum time
- quantum date
- quantum search [query]

---

# 🎭 2. Name Management

- quantum change name to [name]
- quantum rename to [name]
- quantum call yourself [name]

---

# 🖥️ 3. System Controls

## Window Management
- quantum minimize
- quantum maximize
- quantum close window
- quantum lock

## Display & Scrolling
- quantum scroll up
- quantum scroll down
- quantum brightness up
- quantum brightness down

## Audio
- quantum volume up
- quantum volume down
- quantum mute

---

# 📱 4. Application Control

## Open Applications
- quantum open calculator
- quantum open notes
- quantum open safari
- quantum open chrome
- quantum open firefox
- quantum open mail
- quantum open finder
- quantum open terminal
- quantum open settings
- quantum open vscode
- quantum open slack
- quantum open spotify
- quantum open discord
- quantum open zoom
- quantum open [any app]

## Close Applications
- quantum close calculator
- quantum close chrome
- quantum close [app name]
- quantum close window

---

# 🌐 5. Browser Controls

- quantum new tab
- quantum close tab
- quantum incognito
- quantum refresh
- quantum reload

---

# 📝 6. Text & Input

- quantum type [text]
- quantum copy
- quantum paste
- quantum clipboard history
- quantum show clipboard
- quantum clipboard list
- quantum paste item [N]          (e.g. paste item 2)
- quantum paste number [N]
- quantum paste the [ordinal]      (e.g. paste the third item)
- quantum clear clipboard

---

# 📚 7. Information & Search

- quantum wikipedia [topic]
- quantum weather
- quantum weather [city]

---

# 🎵 8. Music Controls

- quantum play music
- quantum pause music
- quantum next song
- quantum next track
- quantum previous song
- quantum previous track

---

# 👆 9. Gesture Recognition

## Activation
- quantum launch gesture recognition
- quantum stop gesture recognition

## Gesture Actions
- V gesture → Move cursor
- Fist → Click and drag
- Pinch → Scroll
- Middle finger up → Left click
- Index finger up → Right click
- Two fingers closed → Double click

## Gesture Settings (UI)
Open the **Settings** panel (gear icon, top-right corner of chat window) to tune:
- Gesture stability (1–10) — higher = less jitter, slower response
- Pinch sensitivity (0.1–0.9) — lower = more sensitive pinch
- Scroll speed (1–10)
- Cursor speed (0.5–5.0)

Changes take effect the next time gesture recognition is started.

---

# 🎮 10. Fun & Utility

- quantum joke
- quantum tell me a joke
- quantum flip a coin
- quantum roll a dice
- quantum timer [minutes]
- quantum set timer [minutes]

---

# 🔋 11. System Information

- quantum battery
- quantum cpu
- quantum system info

---

# 💤 12. Sleep / Wake / Exit

- quantum sleep
- quantum go to sleep
- quantum wake up
- quantum wake
- quantum exit
- quantum quit
- quantum terminate

---

# 📂 13. File Navigation

- quantum list
- quantum open [number]
- quantum back

---

# 📊 14. Quick Calculations

- calculate [expression]
- math [expression]

Examples:
- calculate 25 * 48
- math 50 - 12

---

# 🔄 15. Unit Conversions

- convert [value] [unit] to [unit]

## Distance
- convert 5 km to miles
- convert 5 miles to km
- convert 10 meters to feet
- convert 10 feet to meters
- convert 2 meters to inches
- convert 30 centimeters to inches
- convert 5 inches to centimeters

## Temperature
- convert 25 celsius to fahrenheit
- convert 77 fahrenheit to celsius

## Weight
- convert 70 kg to pounds
- convert 150 pounds to kg
- convert 100 grams to ounces
- convert 5 ounces to grams

## Volume
- convert 2 liters to gallons
- convert 1 gallon to liters
- convert 250 milliliters to fluid ounces
- convert 8 fluid ounces to milliliters

## Speed
- convert 100 km per hour to mph
- convert 60 mph to km per hour

## Data Storage
- convert 512 megabytes to gigabytes
- convert 2 gigabytes to megabytes
- convert 1 gigabyte to terabytes
- convert 1 terabyte to gigabytes

## Time
- convert 2 hours to minutes
- convert 90 minutes to hours
- convert 1 hour to seconds
- convert 3600 seconds to hours
- convert 5 minutes to seconds
- convert 120 seconds to minutes

## Currency (live rates)
- convert 100 usd to inr
- convert 50 eur to gbp
- convert 1000 inr to usd
- Supported: USD, EUR, GBP, INR, JPY, CAD, AUD, CHF, AED

---

# 🌐 16. Enhanced Web Search

## YouTube
- youtube search [query]
- youtube [query]
example: youtube javascript

## GitHub
- github search [query]
- github [query]
example: github javascript

## Stack Overflow
- stackoverflow [query]
example: stackoverflow javascript

## Translation
- translate [text] to [language]
example: translate happy journey to spanish

## Dictionary
- define [word]
example: define javascript

---

# 🌍 17. Network Information

- ip address
- show ip
- wifi name

---

# 🌟 18. Motivation & Facts

- motivational quote
- inspire me
- motivate me
- random fact
- tell me a fact
- fun fact

---

# 🎱 19. Magic 8 Ball

- magic 8 ball [question]
- magic eight ball [question]

---

# 💬 20. Social Interaction

- compliment me
- say something nice
- insult me
- roast me

---

# ❓ 21. Help

- help
- commands
- what can you do

---

# 🎭 22. Personality & Easter Eggs

- quantum sing
- quantum dance
- quantum tell me about yourself
- quantum what do you think about ai
- quantum are you alive
- quantum are you real
- quantum are you conscious

## Appreciation
- good job quantum
- great job
- well done
- thank you

---

# ⚡ 23. Power User System Utilities

- quantum cleanup desktop
- quantum empty recycle bin
- quantum startup apps status
- quantum network speed test

## Confirmation
- confirm
- cancel

---

---

# 🔍 24. File Search & Open by Voice

Search for files and folders anywhere on the computer by name.

- quantum find file [query]
- quantum find folder [query]
- quantum search for file [query]
- quantum find my [query]
- quantum locate file [query]

Returns a numbered list of up to 5 matches. Follow up with:

- quantum open file [N]       (opens the Nth result from the last search)
- quantum open result [N]
- quantum open file [name]    (fresh search + open if single result found)

Examples:
- quantum find file resume
- quantum find my project report
- quantum open file 2

---

# 📋 25. Clipboard History

Tracks the last 10 items copied to the clipboard (auto-monitored in background). History persists across sessions in `~/.quantum_clipboard.json`.

- quantum clipboard history
- quantum show clipboard
- quantum clipboard list        — list recent copied items (numbered)
- quantum paste item [N]        — copy item N back to clipboard and paste it
- quantum paste number [N]
- quantum paste the [ordinal]   — e.g. "paste the second item", "paste the first"
- quantum clear clipboard       — wipe the entire clipboard history

Examples:
- quantum show clipboard
- quantum paste item 3
- quantum paste the first item
- quantum clear clipboard

---

# 🕓 26. Command History & Re-run

All commands you say are tracked in a session history. Use voice commands to replay them, or use the **Up/Down arrow keys** in the chat input to cycle through previous inputs.

- quantum history search [query]    — search history for commands matching [query]
- quantum search history [query]
- quantum run last command           — re-run the most recent non-meta command
- quantum repeat last
- quantum run again
- quantum redo last
- quantum repeat command
- quantum run history [N]            — re-run entry N from last history search results
- quantum run command number [N]
- quantum rerun [N]

**Up/Down arrows in chat input**: cycle through previous commands (shows `↑ History N / total` pill).

Examples:
- quantum history search weather
- quantum run last command
- quantum run history 2

> Note: Meta-commands (run last, repeat, etc.) are excluded from re-run targets to prevent infinite loops.

---

# 🧠 27. LangChain Conversation Memory

When no built-in command matches, Quantum automatically routes the input to the LangChain agent, which has conversation memory (last 8 exchanges) and 9 action tools. You can also manage the memory directly:

- quantum show conversation history   — display recent conversation turns
- quantum conversation history
- quantum what did i say
- quantum clear memory                — wipe all conversation memory
- quantum forget conversation
- quantum reset memory
- quantum memory status               — show how many turns are in memory

## Agent Tools Available
The LangChain agent can automatically call these tools when appropriate:
- `search_web` — opens Google search in browser
- `open_application` — launches an app by name
- `search_files` — finds files on disk
- `get_weather` — current weather for a city
- `calculate` — evaluates math expressions
- `control_volume` — volume up/down/mute/unmute
- `take_screenshot` — saves screenshot to Desktop
- `get_datetime` — current date and time
- `wikipedia_search` — 2-sentence Wikipedia summary

## Configuration
Requires a `.env` file with at least one key:
```
GEMINI_API_KEY=...    # primary LLM (gemini-2.5-flash)
GROQ_API_KEY=...      # fallback LLM (llama-3.3-70b-versatile)
```
Without API keys, unknown commands fall back to static responses silently.

Examples:
- quantum what is the capital of France       → answered via LangChain
- quantum what about its largest city         → uses memory ("its" = France)
- quantum clear memory

---

# ✅ End of Extracted Command Reference