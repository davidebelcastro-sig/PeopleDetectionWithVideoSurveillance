#import socket
import cv2
from PIL import Image
from selenium import webdriver

address = ""
fp = open("file_configurazione.txt","r")
for riga in fp:
    if riga.startswith("address_videocapture"):
        ls = riga.split("=")
        address = ls[1]
   
fp.close()
browser = webdriver.Chrome()
browser.get(address)


volt=0
while 1:
    browser.save_screenshot('salvata.png')
    if volt == 0:
        im = Image.open('salvata.png')
        img = im.crop((50,250,715,650))
        img.save('salvata2.png')
        f = open("appo","w")
        f.close()
        print("invio")
    if volt == 33: #15
        volt=-1
    volt+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
    
