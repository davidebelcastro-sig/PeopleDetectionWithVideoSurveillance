import telebot
import os
import subprocess

state = -1
#open attiva.txt
fp=open("attiva.txt","r")
stringa= fp.read()
fp.close()
if stringa == "on" or stringa == "on\n":
    allarme = 1
else:
    allarme = 0
user_id = ''
API_TOKEN =  ''
fp = open("file_configurazione.txt","r")
for riga in fp:
    if riga.startswith("user_id"):
        ls = riga.split("=")
        user_id = ls[1][:-1]
    elif riga.startswith("key_token"):
        ls = riga.split("=")
        API_TOKEN = ls[1][:-1]
fp.close()
bot = telebot.TeleBot(API_TOKEN)



# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    global state
    global allarme
    #invio condizione allarme
    if message.text== 'help':
        if state == 0:
            bot.send_message(user_id, "programma: on")
        else:
            bot.send_message(user_id, "programma: off")
        if allarme == 1:
            bot.send_message(user_id, "allarme: on")
        else:
            bot.send_message(user_id, "allarme: off")
    elif message.text== 'start' and state == -1:
        os.system("bash eseguibile.sh  & echo $! > file_pid.txt")
        bot.reply_to(message, "programma avviato")
        state = 0
    elif message.text== 'start' and state == 0:
        bot.reply_to(message, "programma già avviato")
    elif message.text== 'stop' and state == 0:
       fp= open("file_pid.txt","r")
       stringa= fp.read()
       pid = ""
       for riga in stringa:
           if riga != '\n':
               pid=pid+riga
       fp.close()
       os.system("pkill -P " + str(pid))
       bot.reply_to(message, "programma con pid " + str(pid) + " interrotto")
       state = -1
    elif message.text== 'stop' and state == -1:
        bot.reply_to(message, "programma non ancora avviato")
    elif message.text== 'ok':
        bot.reply_to(message, "interrotta")
        fp=open("result.txt","w")
        fp.write("1")
        fp.close()
    elif message.text== 'on':
        allarme = 1
        bot.reply_to(message, "allarme on")
        fp= open("attiva.txt","w")
        fp.write("on")
        fp.close()
    elif message.text== 'off':
        allarme = 0
        bot.reply_to(message, "allarme off")
        fp= open("attiva.txt","w")
        fp.write("off")
        fp.close()
    else:
        bot.reply_to(message, "non capisco")

bot.polling()
