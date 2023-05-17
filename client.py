#import socket
import cv2
from PIL import Image
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

address = ""
fp = open("file_configurazione.txt","r")
for riga in fp:
    if riga.startswith("address_videocapture"):
        ls = riga.split("=")
        address = ls[1][:-1]
   
fp.close()
chrome_options = Options()
service = Service('./chromedriver')
browser = webdriver.Chrome(service=service, options=chrome_options)
browser.get(address)


while 1:
    browser.save_screenshot('salvata.png')
    im = Image.open('salvata.png')
    img = im.crop((50,250,715,650))
    img.save('salvata2.png')
    f = open("appo","w")
    f.close()
    print("invio")
    time.sleep(2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
    
