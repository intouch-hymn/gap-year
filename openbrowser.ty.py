#openbrowser.py
import pyautogui
import time
import webbrowser
import pyperclip as cp
chrome = (332,275)
pyautogui.moveTo(332,275,duration=3)
pyautogui.doubleClick(chrome)
url = 'http://www.google.com'
webbrowser.open(url)

time.sleep(3)
pyautogui.write('thailand')

pyautogui.press('enter')

#####
def SearchTH(word):
    time.sleep(3)
    for i in range(7):
        pyautogui.press('tab')

    pyautogui.press('backspace')
    pyautogui.write(word)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.screenshot(word+ '.png')

Search('USA')
Search('china')

