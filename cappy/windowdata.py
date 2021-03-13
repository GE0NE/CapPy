import platform
import psutil
import win32gui
import win32process

windows_version = platform.release()

win10padding = (32,9)
win8padding = (32,9)
win7padding = (30,8)
winxpadding = (30,8)

windows_padding = \
    win10padding if windows_version is '10'\
    else win8padding if windows_version is '8'\
    else win7padding if windows_version is '7'\
    else winxpadding

class SizeData:
    padding = windows_padding
    x,y,w,h = (0,0,0,0)
    def __init__(self, x=0, y=0, w=0, h=0):
        self.x, self.y, self.w, self.h = x, y, w, h

class Window:
    size_data,hwnd,pid,tid,process,name,alive = (None,0,0,0,'','',False)
    def __init__(self, hwnd=0):
        if not hwnd: return
        self.hwnd = hwnd
        self.name = win32gui.GetWindowText(hwnd)
        self.size_data = SizeData()
        self.collect_data()
    def zero(self):
        self.size_data.x,self.size_data.y,\
        self.size_data.w,self.size_data.h,\
        self.hwnd,self.pid,self.tid,self.process,self.name,alive = \
            (0,0,0,0,0,0,0,'','',False)
    def collect_data(self):
        self.tid, self.pid = win32process.GetWindowThreadProcessId(self.hwnd)
        self.alive = self.tid is not 0
        self.process = psutil.Process(self.pid).name()
        dim = win32gui.GetWindowRect(self.hwnd)
        self.size_data.x,self.size_data.y,\
        self.size_data.w,self.size_data.h = \
            (dim[0],dim[1],dim[2],dim[3])
    def update(self):
        if not self.alive: return
        try: self.collect_data()
        except: self.zero()