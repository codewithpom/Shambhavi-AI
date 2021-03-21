import ctypes
import time
def open():

  #to open CD drive
  ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)

def close():
    # to close CD drive
    ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door closed", None, 0, None)



