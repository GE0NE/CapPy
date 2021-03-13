from .windowdata import Window
from .cpy import capture
import cv2

def cv2_display(img, window_name='', wait_time=20):
    color_correction = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imshow('CapPy - %s' % (window_name), color_correction)
    cv2.waitKey(wait_time)

def cv2_record(window):
    frame = capture(window)
    if frame is not None: cv2_display(frame, window_name='%s (%s)' % (window.name, window.process))

def cv2_dispose_window(window_name='CapPy'):
    cv2.destroyWindow(window_name)

def cv2_dispose(window_name=None):
    if not window_name: cv2.destroyAllWindows()
    else: cv2_dispose_window(window_name)