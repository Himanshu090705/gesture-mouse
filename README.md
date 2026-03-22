
Recommended fixes (pick one)
Option A — Using conda (recommended)

Create env and activate:
conda create -n gest39 python=3.10 -y
conda activate gest39
Install deps:
pip install --upgrade pip
pip install -r requirements.txt
Run:
python Gesture_Controller.py --camera 0 --verbose



Create new env with Python 3.10 (recommended)

conda create -n gest39 python=3.10 -y
conda activate gest39
Upgrade pip and install requirements

python -m pip install --upgrade pip
pip install -r requirements.txt
Install PyAudio & pywin32 (Windows)

Option A (conda):
conda install -c anaconda pyaudio -y
conda install pywin32 -y
Option B (if pip install pyaudio fails):
pip install pipwin
pipwin install pyaudio
(Optional) Test camera probe and run app

python Gesture_Controller.py --list-cameras --verbose
python Gesture_Controller.py --camera 0 --verbose
Notes: You can also upgrade your existing env (conda install python=3.10 -n gest) but creating a fresh env is safer.

If you cannot upgrade Python
I can suggest an older mediapipe version that may work on Python 3.8, but it’s fragile and may lack features. Say so if you want that fallback.
Want me to:

generate exact conda/pip commands for your current environment, or
add a short checklist to README.md for setup and common troubleshooting? ✅




Quick note ✅
Thanks — the pip install started. Two small fixes before we proceed:

The earlier python check used mp.file (typo). Use mp.__file__ instead to see the install location.
After the install finishes, run the verification command below and paste the output.
Next actions (run these now) 🧪
If pip install is still running, let it finish. If it finished, show the end of its output (paste it here).
Run this diagnostic command:
python -c "import mediapipe as mp; print('mediapipe', mp.version); print('file=', getattr(mp,'file','N/A')); print('has_solutions=', hasattr(mp,'solutions'))"
If step 2 reports has_solutions = True, run the camera probe:
python Gesture_Controller.py --list-cameras --verbose
If step 2 reports has_solutions = False, try reinstalling a known-compatible combo and paste the install output:
python -m pip uninstall mediapipe -y
python -m pip install mediapipe==0.10.5 protobuf==4.23.4
If you paste the results of step 2 (and any pip output), I’ll give the exact next command and, if needed, the fix for Windows install errors. 🔧

Working commands summary
Say	Does
proton hello	Greeting
proton what is your name	Name
proton date	Today's date
proton time	Current time
proton search [query]	Google search
proton location	Google Maps
proton launch gesture recognition	Starts gesture camera
proton stop gesture recognition	Stops gesture camera
proton list	Lists C:/ files
proton copy	Ctrl+C
proton paste	Ctrl+V
proton bye	Sleep mode
proton exit	Quit

unctionality you could add
Here are some practical additions that fit naturally into the existing structure:

Command idea	What it would do
jarvis open notepad / jarvis open calculator	os.startfile() or subprocess to launch apps
jarvis screenshot	pyautogui.screenshot() — already have pyautogui
jarvis scroll up/down	pyautogui.scroll()
jarvis volume up/down/mute	pycaw — already imported in Gesture_Controller
jarvis wikipedia [topic]	wikipedia.summary() — already imported but unused
jarvis type [text]	pyautogui.typewrite() to dictate text
jarvis minimize / jarvis maximize	pyautogui.hotkey('win', 'd') etc.
jarvis lock	os.system('rundll32.exe user32.dll,LockWorkStation')

mac:
cd "/Users/himanshu/Desktop/final project/gesture-mouse"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-mac.txt
python Gesture_Controller.py
python Quantum.py 

# Gesture Mouse + Quantum Voice Assistant

A Python desktop assistant that combines:

- **Hand gesture mouse control** (cursor, clicks, drag, scroll, volume, brightness)
- **Voice + text commands** through a lightweight **Eel web UI**
- **System, browser, app, utility, and fun commands**

Built with **MediaPipe**, **OpenCV**, **PyAutoGUI**, **SpeechRecognition**, and **Eel**.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
  - [Option A: Conda (Recommended)](#option-a-conda-recommended)
  - [Option B: Virtualenv](#option-b-virtualenv)
- [Run the Project](#run-the-project)
- [How It Works](#how-it-works)
- [Gesture Controls](#gesture-controls)
- [Voice Commands (from `cmds.md`)](#voice-commands-from-cmdsmd)
- [Troubleshooting](#troubleshooting)
- [Customization Guide](#customization-guide)
- [Development Notes](#development-notes)
- [Roadmap Ideas](#roadmap-ideas)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Features

### Gesture Mouse Control
- Cursor movement via hand tracking
- Left click / right click / double click
- Click-and-drag using fist gesture
- Scroll control via pinch
- Volume and brightness control via dominant-hand pinch

### Quantum Assistant
- Wake-word + command flow (`quantum ...`) for voice mode
- Text command input in chat UI
- App open/close commands
- Browser shortcuts (new tab, close tab, refresh, incognito)
- System controls (volume, lock, brightness, etc.)
- Search/information commands (Wikipedia, weather, web search)
- Utility/fun commands (timer, joke, coin flip, dice, motivational quote, etc.)
- Assistant rename support (`change name to ...`)

---

## Project Structure

```bash
.
├── Quantum.py                # Main assistant runtime (voice + command logic + UI thread)
├── Gesture_Controller.py     # Gesture recognition and mouse/system control pipeline
├── app.py                    # Eel chat app bridge (backend for web UI)
├── web/
│   ├── index.html            # UI page
│   ├── js/main.js            # Chat message render + input handlers
│   └── css/...               # Styles
├── cmds.md                   # Extracted command reference (source of command list)
├── QUANTUM_COMMANDS.md       # Detailed command reference
├── GESTURE_GUIDE.md          # Human-friendly gesture tutorial
├── requirements.txt          # Main dependencies (includes Windows-specific libs)
└── requirements-mac.txt      # macOS-oriented dependency list

Requirements
Python 3.9+ (recommended: 3.10)

Webcam for gesture tracking

Microphone for voice mode

Desktop OS support:

Best support currently for Windows and macOS

Some controls are platform-specific (audio/brightness/app launching)

Installation
Choose the setup that fits your environment.

Option A: Conda (Recommended)
conda create -n gest39 python=3.10 -y
conda activate gest39
pip install --upgrade pip
pip install -r requirements.txt
Option B: Virtualenv
Windows (PowerShell / CMD)
python -m venv .venv
.\.venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements-mac.txt
Run the Project
1) Run full assistant (UI + voice/text + commands + gesture launch command)
python Quantum.py
2) Run gesture controller directly (standalone gesture mode)
python Gesture_Controller.py
Optional camera/debug flags (if supported in your current script version):

python Gesture_Controller.py --camera 0 --verbose
python Gesture_Controller.py --list-cameras
Exit keys (gesture window)
ESC or Enter or Q

How It Works
Quantum.py starts the Eel chat interface from app.py.

You can provide input by:

voice (wake-word style), or

text via the chat input box.

Commands are parsed and routed to handlers (system, app, browser, utility, etc.).

Gesture recognition is available via gesture module and related command triggers.

Gesture Controls
Primary gestures
✌️ V gesture → cursor movement mode

✊ Fist → click and drag

🤏 Pinch (dominant hand) → volume/brightness

🤏 Pinch (non-dominant hand) → scrolling

Secondary gestures (after V gesture)
🖕 Middle finger up → left click

☝️ Index finger up → right click

🤞 Two fingers closed → double click

Tips
Use good lighting

Keep hand 1–2 feet from camera

Move steadily for smoother tracking

Voice Commands (from cmds.md)
Default assistant name: quantum
If renamed, use the new name instead.

1) Basic
quantum hello

quantum what is your name

quantum who are you

quantum time

quantum date

quantum search [query]

2) Name Management
quantum change name to [name]

quantum rename to [name]

quantum call yourself [name]

3) System Controls
Window

quantum minimize

quantum maximize

quantum close window

quantum lock

Display / Scroll

quantum scroll up

quantum scroll down

quantum brightness up

quantum brightness down

Audio

quantum volume up

quantum volume down

quantum mute

4) Application Control
Open

quantum open calculator

quantum open notes

quantum open safari

quantum open chrome

quantum open firefox

quantum open mail

quantum open finder

quantum open terminal

quantum open settings

quantum open vscode

quantum open slack

quantum open spotify

quantum open discord

quantum open zoom

quantum open [any app]

Close

quantum close calculator

quantum close chrome

quantum close [app name]

quantum close window

5) Browser
quantum new tab

quantum close tab

quantum incognito

quantum refresh

quantum reload

6) Text/Input
quantum type [text]

quantum copy

quantum paste

7) Information
quantum wikipedia [topic]

quantum weather

quantum weather [city]

8) Music
quantum play music

quantum pause music

quantum next song

quantum next track

quantum previous song

quantum previous track

9) Gesture Recognition Control
quantum launch gesture recognition

quantum stop gesture recognition

10) Fun & Utility
quantum joke

quantum tell me a joke

quantum flip a coin

quantum roll a dice

quantum timer [minutes]

quantum set timer [minutes]

11) System Info
quantum battery

quantum cpu

quantum system info

12) Sleep / Wake / Exit
quantum sleep

quantum go to sleep

quantum wake up

quantum wake

quantum exit

quantum quit

quantum terminate

13) File Navigation
quantum list

quantum open [number]

quantum back

14) Short-form Syntax
open app [name]

close app [name]

list

open [number]

back

time

set timer [minutes]

timer [minutes]

cpu

system info

battery

sleep

go to sleep

wake up

15) Quick Calculations
calculate [expression]

math [expression]

Examples:

calculate 25 * 48

math 50 - 12

16) Unit Conversion
convert [value] [unit] to [unit]

Examples:

convert 5 km to miles

convert 25 celsius to fahrenheit

17) Enhanced Web Search
youtube search [query]

youtube [query]

github search [query]

github [query]

stackoverflow [query]

translate [text] to [language]

define [word]

18) Network
ip address

show ip

wifi name

19) Motivation/Facts
motivational quote

inspire me

motivate me

random fact

tell me a fact

fun fact

20) Magic 8 Ball
magic 8 ball [question]

magic eight ball [question]

21) Social
compliment me

say something nice

insult me

roast me

22) Help
help

commands

what can you do

23) Personality/Easter Eggs
quantum sing

quantum dance

quantum tell me about yourself

quantum what do you think about ai

quantum are you alive

quantum are you real

quantum are you conscious

good job quantum

great job

well done

thank you

Troubleshooting
1) Camera not opening
Try camera list/probe flags if available.

Ensure no other app is locking webcam.

2) Gesture jitter
Improve lighting

Keep steady hand distance

Use smoother movement

3) Mic/voice not recognized
Check microphone permissions

Ensure internet connectivity for online speech recognition backend

Try text mode in chat UI as fallback

4) MediaPipe issues
Reinstall compatible versions:

pip install -U mediapipe protobuf
5) OS-specific command failures
Some app/system commands depend on OS APIs and installed apps.

Windows/macOS behavior may differ.

Customization Guide
Change assistant default name
In Quantum.py, update:

assistant_name = "Quantum"
Add a new command
Add elif block in command handler in Quantum.py

Add command suggestion in app.py (getCommandSuggestions)

Document it in cmds.md and this README

Tune gesture sensitivity
Adjust thresholds/smoothing values in Gesture_Controller.py

Re-test with your camera + lighting setup

Change UI branding
Edit title/text/styles in:

web/index.html

web/css/...

web/js/main.js (behavior only)

Development Notes
Keep command docs centralized in cmds.md and sync README snapshots periodically.

Prefer separating platform-specific actions into helper utilities if command list keeps growing.

If adding LLM features, gate them with clear fallback logic for offline use.

Roadmap Ideas
 Add unit tests for command parser/fuzzy matching

 Add command permission/safety layer (dangerous actions confirmation)

 Add plugin architecture for commands

 Add Linux-focused compatibility matrix

 Add packaged installers (Windows/macOS)

License
Choose one and add it here (MIT / Apache-2.0 / GPL / Proprietary).

Example:

MIT License
Acknowledgements
MediaPipe

OpenCV

PyAutoGUI

Eel

SpeechRecognition

