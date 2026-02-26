# Gesture Control Guide

## How to Use

1. **Start the application** - Your webcam will open showing your hands
2. **Position your hand** in front of the camera
3. **Perform gestures** to control your computer

---

## 🎮 Primary Gestures (Work Independently)

### 1. ✌️ **V-GESTURE** (Peace Sign)
**How:** Index finger + Middle finger extended, other fingers closed
**Function:** **Activate cursor control mode**
**Action:** Move your hand around to control the cursor position

---

### 2. ✊ **FIST**
**How:** All fingers closed in a fist
**Function:** **Click and Drag**
**Action:** Automatically holds down left mouse button while you move your hand
**Use for:** Selecting text, dragging files, drawing

---

### 3. 🤏 **PINCH (Right Hand - Dominant)**
**How:** Thumb + Index finger pinched close together
**Function:** **System Controls**

- **Move hand UP** ⬆️ → **Increase Volume**
- **Move hand DOWN** ⬇️ → **Decrease Volume**
- **Move hand LEFT** ⬅️ → **Decrease Brightness**
- **Move hand RIGHT** ➡️ → **Increase Brightness**

**Note:** Direction is locked after first movement - start fresh pinch to change direction

---

### 4. 🤏 **PINCH (Left Hand - Non-Dominant)**
**How:** Thumb + Index finger pinched close together
**Function:** **Scrolling Controls**

- **Move hand UP** ⬆️ → **Scroll Up**
- **Move hand DOWN** ⬇️ → **Scroll Down**
- **Move hand LEFT** ⬅️ → **Scroll Left** (horizontal scroll)
- **Move hand RIGHT** ➡️ → **Scroll Right** (horizontal scroll)

---

## 🖱️ Secondary Gestures (Require V-Gesture First!)

**IMPORTANT:** You must do a V-gesture first to activate these:

### 5. 🖕 **MIDDLE FINGER** (after V-gesture)
**How:** Only middle finger extended
**Function:** **Left Click**
**Steps:**
1. Do V-gesture to position cursor
2. Change to middle finger → Left click happens

---

### 6. ☝️ **INDEX FINGER** (after V-gesture)
**How:** Only index finger extended
**Function:** **Right Click**
**Steps:**
1. Do V-gesture to position cursor
2. Change to index finger → Right click happens

---

### 7. ✌️ **TWO FINGERS CLOSED** (after V-gesture)
**How:** Index + Middle finger close together (like a closed peace sign)
**Function:** **Double Click**
**Steps:**
1. Do V-gesture to position cursor
2. Bring index and middle fingers close together → Double click happens

---

## 📋 Quick Reference Table

| Gesture | Hand | Function | Notes |
|---------|------|----------|-------|
| ✌️ V-Sign | Either | Move Cursor | Keep it to move mouse |
| ✊ Fist | Either | Drag | Auto-holds left button |
| 🤏 Pinch | RIGHT | Volume/Brightness | Up/Down = Volume, Left/Right = Brightness |
| 🤏 Pinch | LEFT | Scroll | Up/Down = Vertical, Left/Right = Horizontal |
| 🖕 Middle | Either | Left Click | **Need V-gesture first!** |
| ☝️ Index | Either | Right Click | **Need V-gesture first!** |
| ✌️→✊ Two Close | Either | Double Click | **Need V-gesture first!** |
| ✋ Open Palm | Either | Reset/Neutral | Stops all actions |

---

## 💡 Tips for Best Results

1. **Lighting:** Use good lighting so the camera can see your hand clearly
2. **Distance:** Keep your hand 1-2 feet from the camera
3. **Steady Movements:** Move smoothly for best tracking
4. **Clear Gestures:** Make distinct finger positions
5. **Pinch Controls:**
   - Move slowly for fine control
   - Move faster for bigger changes
   - The amount you move = the amount it changes

---

## 🎯 Common Workflows

### **Clicking on Something:**
1. ✌️ V-gesture → move cursor to target
2. 🖕 Middle finger → click

### **Right-Click Menu:**
1. ✌️ V-gesture → move cursor to target
2. ☝️ Index finger → right-click

### **Selecting and Dragging:**
1. ✊ Fist gesture → automatically clicks and holds
2. Move your hand → drags the item
3. ✋ Open palm → releases

### **Adjusting Volume:**
1. 🤏 Pinch with right hand
2. Move up/down to adjust
3. ✋ Open palm to finish

### **Scrolling a Page:**
1. 🤏 Pinch with left hand
2. Move up/down to scroll
3. ✋ Open palm to finish

---

## ⌨️ Keyboard Controls

- **ESC** or **Enter** or **Q** → Exit the application

---

## 🪟 Window Controls

The display window is now **1280x720 pixels** for better visibility. You can:
- **Resize it** by dragging the window corners (it's resizable)
- See your hand tracking with green landmarks and connections
- Monitor which gestures are being detected in real-time

---

## ⚙️ Changing Dominant Hand

By default, **right hand = dominant** (for volume/brightness).
To change this, you would need to modify the code:
```python
dom_hand = True  # Right hand dominant (default)
dom_hand = False # Left hand dominant
```

---

## 🐛 Troubleshooting

**Gestures not detecting:**
- Make sure hand is well-lit
- Keep hand flat facing camera
- Make clear, distinct finger positions

**Cursor is jumpy:**
- Hold your hand more steady
- Ensure good lighting
- Keep hand at consistent distance

**Pinch controls too sensitive:**
- Move your hand more slowly
- Make smaller movements

**Pinch controls not sensitive enough:**
- Move your hand more quickly
- Make larger movements
