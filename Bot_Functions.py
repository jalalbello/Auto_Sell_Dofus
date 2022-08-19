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
    time.sleep(3)

    Transfer_to_inventory_and_type =    [(451, 105),(552, 123),(387, 538)]
    for i in Transfer_to_inventory_and_type:
        pyautogui.leftClick(i)
        time.sleep(7)

    pyautogui.hotkey('ctrl', 'a')
    time.sleep(3)
    pyautogui.press("del")
    time.sleep(3)
    pyautogui.write('obsi', interval=0.25)
    time.sleep(3)

    for i in Transfer_to_inventory_and_type:
        pyautogui.leftClick(i)
        time.sleep(7)

    pyautogui.hotkey('ctrl', 'a')
    time.sleep(3)
    pyautogui.press("del")
    time.sleep(3)
    pyautogui.write('etain', interval=0.25)
    time.sleep(3)

    Transfer_to_inventory_close =    [(451, 105),(552, 123),(1027, 77)]
    for i in Transfer_to_inventory_close:
        pyautogui.leftClick(i)
        time.sleep(7)

    #* to open sacs in inventory
    hot_key_list = [8, 9, 0]
    for i in range(7):
        for i in hot_key_list:
            pyautogui.press(str(i))
            
    enter_back_and_empty_sacs_in_bank=[(766, 293),(713, 493),(871, 100),(839, 105),(891, 113)]
    for i in enter_back_and_empty_sacs_in_bank:
        pyautogui.leftClick(i)
        time.sleep(7)
    #* ressources are in bank after being emptied

def get_potions():

    select_consumables_and_write= [(369, 108), (387, 538)]
    for i in select_consumables_and_write:
        pyautogui.leftClick(i)
        time.sleep(7)
    pyautogui.write('Rappel', interval=0.25)
    time.sleep(3)
    transfer_consumables_and_write= [(451, 105),(552, 123), (304, 538)]
    for i in transfer_consumables_and_write:
        pyautogui.leftClick(i)
        time.sleep(7)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(3)
    pyautogui.press("del")
    time.sleep(3)
    pyautogui.write('bonta', interval=0.25)
    time.sleep(3)
    transfer_potions = [(451, 105), (552, 123)]
    for i in transfer_potions:
        pyautogui.leftClick(i)
        time.sleep(7)

def go_to_hdv_with_ressource(ressource):
    select_resource_and_type =  [(406, 102),(387, 538)]
    for i in select_resource_and_type:
        pyautogui.leftClick(i)
        time.sleep(7)
    pyautogui.write(str(ressource), interval=0.25) 
    time.sleep(3)
    transfer_ressource = [(449, 103),(489, 125)]
    for i in transfer_ressource:
        pyautogui.leftClick(i)
        time.sleep(7)
    leave_bank_go_to_hdv= [(1028, 79),(348, 535),(529, 419),(614, 128)]
    for i in leave_bank_go_to_hdv:
        pyautogui.leftClick(i)
        time.sleep(7)
    #Enter HDV ressource
    click_HdvInZaapi_enter_hdv= [(553, 340),(990, 333)]
    for i in click_HdvInZaapi_enter_hdv:
        pyautogui.doubleClick(i)
        time.sleep(7)

def check_ressource_price_and_sell_it(ressource, sales_number):
    click_sell_and_ressource=[(580, 96),(851, 142)]
    for i in click_sell_and_ressource:
        pyautogui.leftClick(i)
        time.sleep(7)
    quantitiy_100 = pyautogui.locateOnScreen("img/100.png", confidence=0.9, region=(309, 363, 24, 69))
    try:
        x100 = quantitiy_100[0]
        y100 = quantitiy_100[1]
    except:    
        now = time.gmtime()
        timetuple = now[:6]
        hour_min = (timetuple[3], timetuple[4])
        logs = open("logs.txt", "a")
        logs.write(f'Failure to locate 100.png at : {str(hour_min)}\n', "a")

    #*TRANSFORM IMAGE BLOCK
    
    if x100 and y100 is not None: 
        screenshot1 = pyautogui.screenshot("mapcheck1.tiff", region=(x100, y100, 85, 19))
            
        image = cv2.imread("mapcheck1.tiff", 0)
        inverted_image = cv2.bitwise_not(image)
        cv2.imwrite("mapcheck1.tiff", inverted_image)
        img = cv2.imread('mapcheck1.tiff')

        img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
        img = cv2.resize(img, None, fx=2, fy=2)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        kernel = np.ones((1,1), np.uint8)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)
        cv2.imwrite('mapcheck2.tiff', img)
        img = cv2.imread("mapcheck2.tiff", cv2.IMREAD_UNCHANGED)
        scale_percent = 1000 # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)    
        # resize image
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        cv2.imwrite("mapcheck2.tiff", resized)
        thresh = cv2.threshold(cv2.GaussianBlur(resized, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        cv2.imwrite("mapcheck2.tiff", thresh)
        custom_oem = '--psm 12, -c tessedit_char_whitelist=0123456789'

        #*This results in a transformed Image

        #* Transform Image to Text
        custom_oem = '--psm 12, -c tessedit_char_whitelist=0123456789'
        fullstring = pytesseract.image_to_string("mapcheck2.tiff", config=custom_oem)
        numeric_string = re.findall("\d", fullstring)
        price = numeric_string [3:]
        #! transform price into a str and remove spaces
        price = " ".join(price).replace(" ","")
        Price_History = open("Price_History.txt", "a")
        nl = "\n"
        Price_History.write(f'{nl}{ressource} price is : {str(price)}')
        final_price= int(price) - 1

        #! since gold price is unchangable
        if ressource != 'or':
            pyautogui.moveTo(31, 36)
            #move so the ressoruce definitions don't obstruct our operation
            time.sleep(3)
            pyautogui.leftClick (671, 132)
            time.sleep(3)
            pyautogui.write(str(ressource), interval=0.25)
            pyautogui.leftClick (778, 154)
            pyautogui.write(str(final_price), interval=0.25)
            pyautogui.press('enter')
            confirm_price_change = pyautogui.locateOnScreen("img/yes.png", confidence=0.75)
            if confirm_price_change is not None : pyautogui.leftClick(confirm_price_change)
            time.sleep(5)
            pyautogui.leftClick(1026, 63)
            time.sleep(5)
            pyautogui.leftClick(990, 333)
            time.sleep(20)
            for i in click_sell_and_ressource:
                pyautogui.leftClick(i)
                time.sleep(7)
        #!so the bot changes the price if the ressource is not gold, and leaves and selects it again, if ressource is gold then its already selected and its gonna start the sale   
        pyautogui.write(str(final_price), interval=0.25)

        for i in range (sales_number) :
            sell = pyautogui.locateOnScreen("img/sell.png", confidence=0.99)
            pyautogui.click(sell)
            time.sleep(3)
        #! xno in case there is an error prompt
        time.sleep(2)
        xno = pyautogui.locateOnScreen("img/xno.png", confidence=0.99)
        if xno is not None: pyautogui.click(xno)

        time.sleep(7)
        pyautogui.leftClick(1026, 63)
        