import pyautogui
import time
import pytesseract
import cv2
import re
import numpy as np
from pytesseract import *
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import Bot_Functions


pyautogui.PAUSE = 0
Bot_Functions.empty_inventory()
#! empty sac just once
Bot_Functions.emptysac()
Bot_Functions.get_potions()
Bot_Functions.go_to_hdv_with_ressource("Etain")
Bot_Functions.check_ressource_price_and_sell_it("Etain", 15)

Bot_Functions.empty_inventory()
Bot_Functions.get_potions()
Bot_Functions.go_to_hdv_with_ressource("Obidienne")
Bot_Functions.check_ressource_price_and_sell_it("Obidienne", 15)