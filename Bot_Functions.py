import pyautogui
import time
import pytesseract
import cv2
import re
import numpy as np
from pytesseract import *
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def empty_inventory():
    pyautogui.press("4")
    time.sleep(10)
    xy = [(1043, 636), (629, 459),  (766, 293), (713, 493), (871, 100), (839, 105), (891, 113)]
    for i in xy:
        pyautogui.leftClick(i)
        time.sleep(7)
    #! Inventory is empty

def emptysac():

    xy =[(369, 108), (387, 538)]

    for i in xy:
        pyautogui.leftClick(i)
        time.sleep(7)

    pyautogui.write('d\'or', interval=0.25)

    Transfer_to_inventory_and_type =    [(451, 105),(552, 123),(387, 538)]
    for i in Transfer_to_inventory_and_type:
        pyautogui.leftClick(i)
        time.sleep(7)

    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press("del")
    pyautogui.write('obsi', interval=0.25)

    for i in Transfer_to_inventory_and_type:
        pyautogui.leftClick(i)
        time.sleep(7)

    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press("del")
    pyautogui.write('etain', interval=0.25)

    Transfer_to_inventory_close =    [(451, 105),(552, 123),(1027, 77)]
    for i in Transfer_to_inventory_close:
        pyautogui.leftClick(i)
        time.sleep(7)

    #* to open sacs in inventory
    hot_key_list = [8, 9, 0]
    for i in range(7):
        for i in hot_key_list:
            pyautogui.press(str(i))
            
    #!enter back and empty sacs in bank

(369, 108), (387, 538),}
pyautogui.write('Rappel', interval=0.25)
{(451, 105),(552, 123), }
pyautogui.doubleClick(304, 538)
pyautogui.press("del")
pyautogui.write('bonta', interval=0.25)
{(451, 105), (552, 123), (406, 102), (387, 538), }
pyautogui.write(Ressource, interval=0.25) 
{(449, 103),(489, 125),(1028, 79),(348, 535),(529, 419),(614, 128),}

class GetPrice:
    def __init__(self, ressource):
        self.ressource = ressource
        pyautogui.doubleClick(553, 340)
print("HDV ressource")

