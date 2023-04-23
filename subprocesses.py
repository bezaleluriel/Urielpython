import os

import pyautogui as pyautogui
import subprocess

# x = subprocess.run('calc.exe')
# print(x.returncode)
# x = subprocess.call(['notepad.exe', r'C:\Users\MHT\Desktop\1.txt'])
# print(x.returncode)


x = subprocess.Popen('notepad.exe')
input('close it?')
os.system('taskkill /f /im notepad.exe')

