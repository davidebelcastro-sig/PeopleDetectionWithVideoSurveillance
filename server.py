# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 19:29:41 2022

@author: david
"""

#import socket
#import threading
import numpy as np
import cv2
#import pywhatkit
import telegram
import time
import datetime
import os



def getOrario():
    now = str(time.strftime("%H%M"))  #capire come da orario a mezanotte,se 24:00:00 o 00:00:00 o 0:00:00
    ora=now[:-2]
    mini=now[2:]
    orario=ora+":" + mini +":00"
    timeList = [orario,"04:00:00"]
    mysum = datetime.timedelta()
    for i in timeList:
        (h, m, s) = i.split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        mysum += d
    return str(mysum)
    
nextOra=getOrario()
nextOra=nextOra[:-3]
oraList=[nextOra]


#get this from telegram
api_key = ''
user_id = ''
try:
    f = open("appo","r")
    f.close()
    os.remove("appo")
except:
     pass




    
def processMessages(net,output_layers):
    i=0
    k=0
    while True:
            while True:
                try:
                    f = open("appo","r")
                    f.close()
                    os.remove("appo")
                    print("preso")
                    break
                except:
                     
                     pass
            trov=0
            allarme = 0
            fp = open("attiva.txt","r")
            for f in fp:
                if f == "on":
                    allarme = 1
            fp.close()
            img = cv2.imread("salvata2.png",1)
            if allarme == 1:
                blob=cv2.dnn.blobFromImage(img,0.00392,(416,416),(0,0,0),True,crop=False)
                net.setInput(blob)
                #invio a web server
                outs=net.forward(output_layers)   #è questa la piu lenta
                #prendi outs da web server
                for output in outs:
                    for detection in output:
                    #Detecting confidence in 3 steps
                        scores=detection[5:]                
                        class_id=np.argmax(scores)          
                        confidence =scores[class_id]      
                        if confidence > 0.8 and class_id == 0: #Means if the object is detected
                            trov=1 
                            #break 
                    #if trov == 1:
                        #break
            if trov == 1:
                bot = telegram.Bot(token=api_key)
                bot.send_message(chat_id=user_id, text='ATTENZIONE!!!!!!!!!!!!\nRILEVATA PERSONA')
                bot.sendPhoto(chat_id=user_id, photo=open("salvata2.png","rb"))
                os.system("python music.py")
                            
                #ricevo da utente messaggio di bloccare il suono
            if str(time.strftime("%H%M")) in oraList:
                bot = telegram.Bot(token=api_key)
                bot.send_message(chat_id=user_id, text='Tutto ok,il programma è ancora in esecuzione')
                oraList.remove(oraList[0])
                nextOra=getOrario()
                nextOra=nextOra[:-3]
                oraList.append(nextOra)
            print("analizzato")



net=cv2.dnn.readNet("yolov3.weights","yolov3.cfg")
classes=[]
with open("coco.names","r") as f:
    read=f.readlines()
for i in range(len(read)):
    classes.append(read[i].strip("\n"))
layer_names=net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
processMessages(net, output_layers)

    
