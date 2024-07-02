from pyautogui import *
import pyautogui
import cv2
import numpy as np
import time
import keyboard
import win32api, win32con
import threading

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.005)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

print("started")

targetImg = cv2.imread(r"C:\Users\semih\Projects\python-exercises\Exercise Scripts\clickBot\target.png")

stop_event = threading.Event()

def checkStop():
    while not stop_event.is_set():
        if keyboard.is_pressed('q'):
            stop_event.set()
        time.sleep(0.05)

def scan(region):
    time.sleep(region[1]/1000)
    while not stop_event.is_set():
        # contours = []  #Buna muhtemelen gerek yok
        scrSht = np.array(pyautogui.screenshot(region=region))
        scrHsv = cv2.cvtColor(scrSht, cv2.COLOR_RGB2HSV)
        maskGreen = cv2.inRange(scrHsv, (29, 85, 215), (47,255,255))
        # imaskGreen = maskGreen > 0
        # green = np.zeros_like(screen, np.uint8)
        # green[imaskGreen] = screen[imaskGreen]

        cv2.imshow("maskGreen "+str(region), maskGreen)
        cv2.waitKey(1)
        
        contours, _ = cv2.findContours(maskGreen, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

        # Iterate through each contour and find its center
        for contour in contours:

            if cv2.contourArea(contour) >= 60:
                # Compute the moments of the contour
                M = cv2.moments(contour)
                
                # Calculate the center of the contour
                if M["m00"] != 0:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    
                    # Click on the center of the contour *using PyAutoGUI*
                    click(5+cX, 140+cY+18)
                    time.sleep(0.001)

                    # For visualization purposes (optional)
                    # cv2.circle(maskGreen, (cX, cY), 5, (255, 0, 0), -1)
        time.sleep(0.01)
        # Display the result (optional)
        # cv2.imshow('Centers ', maskGreen)
        # cv2.waitKey(1)

# regions = [(5, 140, 440, 205), (5, 345, 440, 205), (5, 550, 440, 205), (5, 755, 440, 205)]
region = (5,140,440,820)

threads = [threading.Thread(target=checkStop), threading.Thread(target=scan, args=(region,))]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("quit")