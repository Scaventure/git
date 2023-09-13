import pyautogui
import win32clipboard
import string
import time
import os
from selenium import webdriver

driver = webdriver.Chrome

os.chdir(r'C:\Users\adminwaan\Documents\git\GD Scrape')

COs = [60]

for i in COs:

    res = pyautogui.locateCenterOnScreen("co_list.png")
    pyautogui.moveTo(res[0],res[1],duration = 2)
    pyautogui.leftClick()
    pyautogui.press('home')
    
    for j in range(1, i):
        pyautogui.press('down')

    pyautogui.press('tab')

    time.sleep(2)

    pyautogui.hotkey('ctrl', 'u')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    win32clipboard.OpenClipboard()
    pagecode = win32clipboard.GetClipboardData()
    email = pagecode.split('Security Focal Points')[1]
    email = email.split('Office Last Verified')[0]
    print(email)
    pyautogui.hotkey('ctrl', 'w')


# Test GIT

