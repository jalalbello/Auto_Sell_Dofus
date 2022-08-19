import pyautogui
import pytesseract
import numpy as np
from pytesseract import *
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import Bot_Functions

#! carefull the bot changes price for old items each time it goes to sell

pyautogui.PAUSE = 0

Bot_Functions.empty_inventory()
# ! empty sac just once
Bot_Functions.emptysac()
Bot_Functions.get_potions()
Bot_Functions.go_to_hdv_with_ressource("Etain")
Bot_Functions.check_ressource_price_and_sell_it("Etain", 15)

Bot_Functions.empty_inventory()
Bot_Functions.get_potions()
Bot_Functions.go_to_hdv_with_ressource("Obsidienne")
Bot_Functions.check_ressource_price_and_sell_it("Obsidienne", 15)

Bot_Functions.empty_inventory()
Bot_Functions.get_potions()
Bot_Functions.go_to_hdv_with_ressource("or")
Bot_Functions.check_ressource_price_and_sell_it("or", 15)