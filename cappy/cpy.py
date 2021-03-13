from .windowdata import SizeData, Window
from threading import Thread
from PIL import ImageGrab
import numpy as np
import win32gui
import sys

def capture(window, output_frame=np.zeros(1)):
    Thread(target=_capture, args=(window, output_frame)).start()
    return frame

def _capture(window, frame=np.zeros(1))
    if not isinstance(window, Window): return
    window.update()
    if not window.tid: return
    pt, pb = window.size_data.padding
    frame = np.array(ImageGrab.grab(bbox=(window.size_data.x+pb, window.size_data.y+pt,\
        window.size_data.w-pb + 1 if window.size_data.x+pb <= window.size_data.w-pb else 0,\
        window.size_data.h-pb + 1 if window.size_data.y+pt <= window.size_data.h-pb else 0)))
    return frame

def retrieve_windows(out):
    if not isinstance(out, list): return
    win32gui.EnumWindows(lambda hwnd,lst: lst.append( Window(hwnd) ), out)

def match_window(process):
    windows = []
    retrieve_windows(windows)
    for window in windows:
        if process == window.process:
            print('Found process:', process)
            return window
    print('Could not find process:', process)
    return None