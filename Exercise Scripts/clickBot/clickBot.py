from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import threading

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.003)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


print("started")

targetImg = r"C:\Users\semih\Projects\python-exercises\Exercise Scripts\clickBot\target.png"

        

def scan1():
    while not keyboard.is_pressed('q'):
        try:
            target = pyautogui.locateCenterOnScreen(targetImg, confidence=0.83, region=(5,140,420,205))
            click(target[0],target[1]+20)
            time.sleep(0.08)
        except pyautogui.ImageNotFoundException:
            continue

def scan2():
    while not keyboard.is_pressed('q'):
        try:
            target = pyautogui.locateCenterOnScreen(targetImg, confidence=0.83, region=(5,345,420,205))
            click(target[0],target[1]+20)
            time.sleep(0.08)
        except pyautogui.ImageNotFoundException:
            continue

def scan3():
    while not keyboard.is_pressed('q'):
        try:
            target = pyautogui.locateCenterOnScreen(targetImg, confidence=0.83, region=(5,550,420,205))
            click(target[0],target[1]+20)
            time.sleep(0.08)
        except pyautogui.ImageNotFoundException:
            continue

def scan4():
    while not keyboard.is_pressed('q'):
        try:
            target = pyautogui.locateCenterOnScreen(targetImg, confidence=0.83, region=(5,755,420,205))
            click(target[0],target[1]+20)
            time.sleep(0.08)
        except pyautogui.ImageNotFoundException:
            continue


thread_1 = threading.Thread(target=scan1)
thread_2 = threading.Thread(target=scan2)
thread_3 = threading.Thread(target=scan3)
thread_4 = threading.Thread(target=scan4)

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()


print("quit")