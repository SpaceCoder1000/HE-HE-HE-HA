import ctypes
import time

VK_LWIN = 0x5B 
VK_M = 0x4D 
VK_ALT = 0x12  
VK_F4 = 0x73   
VK_ENTER = 0x0D 

# Simulate Windows + M
ctypes.windll.user32.keybd_event(VK_LWIN, 0, 0, 0)  # Press down Windows key
ctypes.windll.user32.keybd_event(VK_M, 0, 0, 0)      # Press down M key
ctypes.windll.user32.keybd_event(VK_M, 0, 2, 0)      # Release M key
ctypes.windll.user32.keybd_event(VK_LWIN, 0, 2, 0)   # Release Windows key

# Add a short delay to ensure the system processes the previous keys
time.sleep(0.5)

# Simulate Alt + F4
ctypes.windll.user32.keybd_event(VK_ALT, 0, 0, 0)    # Press down Alt key
ctypes.windll.user32.keybd_event(VK_F4, 0, 0, 0)      # Press down F4 key
ctypes.windll.user32.keybd_event(VK_F4, 0, 2, 0)      # Release F4 key
ctypes.windll.user32.keybd_event(VK_ALT, 0, 2, 0)     # Release Alt key

# Add a short delay to ensure the system processes the previous keys
time.sleep(0.5)

# Simulate Enter key
ctypes.windll.user32.keybd_event(VK_ENTER, 0, 0, 0)   # Press down Enter key
ctypes.windll.user32.keybd_event(VK_ENTER, 0, 2, 0)   # Release Enter key
