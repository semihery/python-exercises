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
    time.sleep(0.002)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


print("started")

while not keyboard.is_pressed('q'):
    try:
        target = pyautogui.locateCenterOnScreen(r"C:\Users\semih\Projects\python-exercises\Exercise Scripts\clickBot\target.png", confidence=0.70, region=(5,120,420,780))
        click(target[0],target[1]+15)
    except pyautogui.ImageNotFoundException:
        continue


print("quit")











""" 
def scan(i):
    
    print("thread_{} başlatıldı".format(i))

    while keyboard.is_pressed('q') == False:
        pic = pyautogui.screenshot(region=(5,240+80*i,420,1))

        for x in range(420):
                r,g,b = pic.getpixel((x,0))
                if 195<r<220 and 215<g<250 and b<100:   # 193<r<210 and 215<g<235 and b<10:
                    click(5+x,255+80*i)
                    break

    print("thread_{} durduruldu".format(i))
    

thread_0 = threading.Thread(target=scan,args=(0,))
thread_1 = threading.Thread(target=scan,args=(1,))
thread_2 = threading.Thread(target=scan,args=(2,))
thread_3 = threading.Thread(target=scan,args=(3,))

thread_0.start()
thread_1.start()
thread_2.start()
thread_3.start()

thread_0.join()
thread_1.join()
thread_2.join()
thread_3.join()
"""





# while keyboard.is_pressed('q') == False:
#     print("rev")
#     pic = pyautogui.screenshot(region=(5,240,420,20))
    # pic.save(r"C:\Users\semih\OneDrive\Resimler\Ekran Görüntüleri\savedImage.png")

    # for y in range(0,20,2):
    #     for x in range(0,420,2):
    #         r,g,b = pic.getpixel((x,y))
    #         if 195<r<208 and 220<g<245 and b<11:
    #             click(5+x,270+y)
    #             time.sleep(0.05)





# 150,225  200,260  0,50  RENK ARALIGI R,R G,G B,B
# 5,180   425,180  
# 5,580   425,580