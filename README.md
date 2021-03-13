# CapPy
A Pillow wrapper for easy window capturing and window data acquisition.

Examples:
```
import cappy as cpy
window = cpy.match_window('notepad.exe')
```
---
```
import cappy as cpy
window = cpy.match_window('mspaint.exe')
print(window.process, window.pid, window.tid, window.hwnd)
>mspaint.exe 9024 6024 1048826
```
---
```
import cappy as cpy
window = cpy.match_window('GTA5.exe')
while(window.alive):
    cpy.cv2_record(window)
cpy.cv2_dispose()
```
---
```
import cappy as cpy
windows_out = []
cpy.retrieve_windows(windows_out)
for window in windows_out:
    print(window.name)
>Calculator
>Untitled - Notepad
>#general - Discord
>Google - Mozilla Firefox
>Steam
>...
```