from curses import window
from multiprocessing import Condition
from os import mkdir
import cv2
import numpy as np
import pyautogui

import win32gui
import win32con
import time
from os import mkdir

try:
    mkdir("recordings")
except FileExistsError:
    pass

def minimzeWindow():
    window = win32gui.FindWindow(None, "Screen recorder")
    win32gui.ShowWindow(window, win32con.SW_MINIMIZE)





#display screen resolution, get it from ur os settings
SCREEN_SIZE = (1366, 768)
#define the codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")
#create the video write object
output = cv2.VideoWriter("recordings/"+"ScreenRecording "+time.strftime("%H-%M-%S-%d-%m-%y")+".mp4",fourcc, 20.0,(SCREEN_SIZE))

print("Recording startted .. \n Window minimised in taskbar.\n press q to exit.")

minimized = False

Done = False 
while not Done:
    #make a ascreenshot
    img = pyautogui.screenshot()
    #convert thesr pixels to a proer numpy array to work withOpenCv
    frame = np.array(img)
    #convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #show the frame
    cv2.imshow("Screen recorder", frame)

    if minimized == True:
        pass
    else:
        minimized = True
        minimzeWindow()

    #write the frame
    output.write(frame)
    #if the user clicks q, it exits
    #open the screen recorder and press 'q'
    if cv2.waitKey(1) == ord("q"):
        Done = True
        print("\rRecording Finished.")
        break
#make sure every thing is closed when exited
output.release()
cv2.destroyAllWindows()