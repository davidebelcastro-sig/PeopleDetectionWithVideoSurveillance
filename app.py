from tkinter import *
from selenium import webdriver
import subprocess

address = "" 
fp = open("file_configurazione.txt","r")
for riga in fp:
    if riga.startswith("address_videocapture"):
        ls = riga.split("=")
        address = ls[1]
   
fp.close()

def esci(g):
    g.destroy()

def lancia(n):
    browser = webdriver.Chrome()
    browser.get(address)
    if n == 0:
        gui.destroy()
        gui2 = Tk()
        gui2.configure(background="light green")
        gui2.title("ALLARME")
        gui2.geometry("500x500")
        button1 = Button(gui2, text='Attiva allarme', fg='black', bg='red',
command=lambda: start(gui2,browser), height=4, width=50)
        button1.grid(row=2, column=0)
   
        button3 = Button(gui2, text='Chiudi connessione', fg='black', bg='red',
command=lambda: inizio(gui2,browser), height=4, width=50)
        button3.grid(row=4, column=0)
        gui2.mainloop()
       
    else:
        button1 = Button(n, text='Attiva allarme', fg='black', bg='red',
command=lambda: start(n,browser), height=4, width=50)
        button1.grid(row=2, column=0)
   
        button3 = Button(n, text='Chiudi connessione', fg='black', bg='red',
command=lambda: inizio(n,browser), height=4, width=50)
        button3.grid(row=4, column=0)
        n.mainloop()
   




def start(n,browser):
   
    button2 = Button(n, text='Disattiva allarme', fg='black', bg='green',
command=lambda: disat(n,browser), height=4, width=50)
    button2.grid(row=2, column=0)
   
    button3 = Button(n, text='Chiudi connessione', fg='black', bg='red',
command=lambda: inizio(n,browser), height=4, width=50)
    button3.grid(row=4, column=0)
    #lancio il programma effettivo
    try:
        browser.close()
    except:
        pass
    subprocess.run(["bash", "eseguibile.sh"])
       




def disat(n,browser):
    #blocco il programma e rendo solo la visibilità della videocamera
    #CHIUDERE PROGRAMMA
    #attivare solo il browser
    #segnale control c + fg + segnale control c
    
    browser = webdriver.Chrome()
    browser.get(address)
    button2 = Button(n, text='Attiva allarme', fg='black', bg='red',
command=lambda: start(n,browser), height=4, width=50)
    button2.grid(row=2, column=0)
   
    button3 = Button(n, text='Chiudi connessione', fg='black', bg='red',
command=lambda: inizio(n,browser), height=4, width=50)
    button3.grid(row=4, column=0)
    
    

def close(h):
    try:
        h.close()
    except:
        pass
   
def inizio(n,browser):
    close(browser)
    n.destroy()
    gui3 = Tk()
    gui3.configure(background="light green")
    gui3.title("ALLARME")
    gui3.geometry("500x500")
    button1 = Button(gui3, text='Attiva Connessione', fg='black', bg='red',
command=lambda: lancia(gui3), height=4, width=50)
    button1.grid(row=2, column=0)
    button2 = Button(gui3, text='Exit', fg='black', bg='red',
command=lambda: esci(gui3), height=4, width=50)
    button2.grid(row=4, column=0)





gui = Tk()
gui.configure(background="light green")
gui.title("ALLARME")
gui.geometry("500x500")
   
   
button1 = Button(gui, text='Attiva Connessione', fg='black', bg='red',
command=lambda: lancia(0), height=4, width=50)
button1.grid(row=2, column=0)
button2 = Button(gui, text='Exit', fg='black', bg='red',
command=lambda: esci(gui), height=4, width=50)
button2.grid(row=4, column=0)


gui.mainloop()
