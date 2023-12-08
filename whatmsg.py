import pyautogui
import time
time.sleep(3)
count=0
while count<=20:
    pyautogui.typewrite("hi ")
    pyautogui.press("shift")
    count=count+1
 
