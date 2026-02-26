"""
Utility Functions

Helper functions for the gesture control system.
"""

import cv2


def list_cameras(max_index=5):
    """
    Probe camera indices from 0 to max_index-1 and print availability.

    Parameters
    ----------
    max_index : int
        Maximum camera index to probe (default: 5)

    Returns
    -------
    None
    """
    print(f"Probing camera indices 0..{max_index-1} ...", flush=True)
    for i in range(max_index):
        # On Windows DirectShow backend may improve detection
        cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
        opened = cap.isOpened()
        print(f"  index {i}: {'AVAILABLE' if opened else 'not available'}", flush=True)
        if opened:
            cap.release()
