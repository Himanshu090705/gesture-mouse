"""
Gesture and Hand Label Enumerations

Defines all gesture types and hand labels used in the gesture control system.
"""

from enum import IntEnum


class Gest(IntEnum):
    """
    Enum for mapping all hand gestures to binary numbers.

    Binary encoded gestures based on finger states:
    - FIST: All fingers closed (0)
    - PINKY: Only pinky open (1)
    - RING: Only ring finger open (2)
    - MID: Only middle finger open (4)
    - INDEX: Only index finger open (8)
    - THUMB: Only thumb open (16)
    - PALM: All fingers open (31)

    Special gestures:
    - V_GEST: Peace sign (33)
    - TWO_FINGER_CLOSED: Two fingers close together (34)
    - PINCH_MAJOR: Pinch gesture on dominant hand (35)
    - PINCH_MINOR: Pinch gesture on non-dominant hand (36)
    """

    # Binary Encoded
    FIST = 0
    PINKY = 1
    RING = 2
    MID = 4
    LAST3 = 7
    INDEX = 8
    FIRST2 = 12
    LAST4 = 15
    THUMB = 16
    PALM = 31

    # Extra Mappings
    V_GEST = 33
    TWO_FINGER_CLOSED = 34
    PINCH_MAJOR = 35
    PINCH_MINOR = 36


class HLabel(IntEnum):
    """
    Multi-handedness Labels.

    Defines which hand is major (dominant) and which is minor (non-dominant).
    By default: Right hand = MAJOR, Left hand = MINOR
    """
    MINOR = 0
    MAJOR = 1
