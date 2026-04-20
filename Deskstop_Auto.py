import pyautogui
import time



pyautogui.hotkey('min', 'r')
pyautogui.press('enter')
time.sleep(2)

pyautogui.write("hello world! is automated text file. ", interval=0.1)

pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.write('automoted_file.txt', interval=0.1)
pyautogui.press('enter')
time.sleep(1)

pyautogui.hotkey('alt', 'f4')
pyautogui.press('enter')

