# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Hand gesture-controlled mouse application using computer vision. Uses MediaPipe for hand tracking, OpenCV for video capture, and PyAutoGUI for mouse/system control. Single-file Python application.

## Setup and Running

### Environment Requirements
- **Python 3.9+** (MediaPipe requires modern typing features)
- Windows-specific dependencies (pycaw for audio, screen-brightness-control)

### Initial Setup

Using conda (recommended):
```bash
conda create -n gest39 python=3.10 -y
conda activate gest39
pip install --upgrade pip
pip install -r requirements.txt
```

Using venv:
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### Running the Application

```bash
# Run with default camera (index 0)
python Gesture_Controller.py

# Run with specific camera index and verbose logging
python Gesture_Controller.py --camera 0 --verbose

# List available cameras
python Gesture_Controller.py --list-cameras
```

Exit the application by pressing ESC, Enter, or 'q' in the video window.

## Architecture

### Core Components

The application is structured as a single-file monolith ([Gesture_Controller.py](Gesture_Controller.py)) with four main classes:

1. **Gest (IntEnum)** - Binary-encoded gesture definitions
   - Uses bit flags for finger states (FIST=0, PINKY=1, RING=2, MID=4, INDEX=8, THUMB=16, PALM=31)
   - Special gestures: V_GEST, TWO_FINGER_CLOSED, PINCH_MAJOR, PINCH_MINOR

2. **HandRecog** - Gesture recognition from MediaPipe landmarks
   - Converts hand landmarks to binary finger states
   - Implements noise filtering with frame counting (requires 5 consistent frames)
   - Methods: `set_finger_state()`, `get_gesture()`, distance calculations

3. **Controller** - System control execution (static class)
   - Mouse control: `get_position()` with dampening for stability
   - Pinch gestures: `pinch_control()` detects direction (horizontal/vertical)
   - System controls: `changesystemvolume()`, `changesystembrightness()`
   - Scroll controls: `scrollVertical()`, `scrollHorizontal()`

4. **GestureController** - Main orchestrator and camera handler
   - Manages video capture via OpenCV
   - Processes frames with MediaPipe Hands (max 2 hands)
   - Routes gestures to appropriate handlers
   - Major/minor hand classification (right hand = major by default)

### Gesture Control Flow

```
Camera Frame → MediaPipe Hands → classify_hands() → HandRecog (major/minor)
                                                    ↓
                                              set_finger_state()
                                                    ↓
                                               get_gesture()
                                                    ↓
                                          Controller.handle_controls()
                                                    ↓
                                    System Actions (mouse, click, scroll, volume, brightness)
```

### Gesture Mappings

The application uses a two-stage gesture system:

**Primary gestures:**
- **V_GEST** (peace sign) → Activates cursor control mode (sets Controller.flag)
- **FIST** → Click and drag (mouseDown + move)
- **PINCH_MINOR** (non-dominant hand) → Scroll control
- **PINCH_MAJOR** (dominant hand) → Volume/brightness control

**Secondary gestures (require V_GEST first):**
- **MID** (middle finger) → Left click
- **INDEX** (index finger) → Right click
- **TWO_FINGER_CLOSED** → Double click

### Hand Recognition Details

- **Dominant hand (dom_hand)**: Right hand by default → becomes `hr_major`
- **Gesture priority**: PINCH_MINOR checked first, then major hand gestures
- **Cursor stabilization**: Dampening algorithm in `get_position()` reduces jitter
  - Small movements (distsq ≤ 25): ignored (ratio=0)
  - Medium movements (25 < distsq ≤ 900): scaled by 0.07*√distsq
  - Large movements (distsq > 900): scaled by 2.1

### Pinch Control Mechanism

Pinch gestures use quantized displacement from start position:
- Threshold: 0.3 units for direction detection
- Requires 5 consistent frames before triggering action
- Direction determined by larger axis (x or y)
- PINCH_MAJOR: x-axis → brightness, y-axis → volume
- PINCH_MINOR: x-axis → horizontal scroll, y-axis → vertical scroll

## Common Issues

### Camera Access
If camera fails to open, use `--list-cameras` to probe available indices. On Windows, the code uses DirectShow backend (CAP_DSHOW) for better detection.

### MediaPipe Compatibility
The code validates `mp.solutions` exists. If missing, it indicates incompatible MediaPipe build - reinstall with: `pip install mediapipe==0.10.5 protobuf -U`

### Windows-Specific Dependencies
- **pycaw**: Audio control (may require `comtypes`)
- **screen-brightness-control**: Display brightness control
- Both require Windows APIs and won't work on Linux/macOS

## Development Notes

### Making Changes to Gestures

To add new gestures:
1. Add enum value to `Gest` class
2. Implement detection logic in `HandRecog.get_gesture()`
3. Add handler case in `Controller.handle_controls()`
4. Consider noise filtering needs (current threshold: 5 frames)

### Modifying Control Behavior

- **Cursor speed/sensitivity**: Adjust dampening ratios in `Controller.get_position()`
- **Pinch sensitivity**: Modify `Controller.pinch_threshold` (default: 0.3)
- **Gesture stability**: Change frame_count threshold in `HandRecog.get_gesture()` (default: 4)

### Camera Configuration

MediaPipe Hands parameters in `GestureController.start()`:
- `max_num_hands=2`: Supports both hands
- `min_detection_confidence=0.5`: Hand detection threshold
- `min_tracking_confidence=0.5`: Tracking threshold

## Logging

The application logs to `gesture_controller_start.log` for:
- Startup events and camera index selection
- Python version check failures
- Import errors with full tracebacks
- Camera probe results

Use `--verbose` flag for runtime logging to stdout.
