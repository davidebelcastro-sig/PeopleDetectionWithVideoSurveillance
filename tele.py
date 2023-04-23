

import telebot
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

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text== 'ok':
        bot.reply_to(message, "interrotta")
        fp=open("result.txt","w")
        fp.write("1")
        fp.close()
    elif message.text== 'on':
        bot.reply_to(message, "allarme on")
        fp= open("attiva.txt","w")
        fp.write("on")
        fp.close()
    elif message.text== 'off':
        bot.reply_to(message, "allarme off")
        fp= open("attiva.txt","w")
        fp.write("off")
        fp.close()
    elif message.text== 'sirena':
        bot.reply_to(message, "sirena attivata")
        fp=open("result.txt","w")
        fp.close()
    else:
        bot.reply_to(message, "non capisco")

bot.polling()
