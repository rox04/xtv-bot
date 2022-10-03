import requests,user_agent,json,flask,telebot,random,re,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start'])
def boten(message):



    mas = types.InlineKeyboardMarkup(row_width=2)

    A = types.InlineKeyboardButton(text ="USER (BFFFL)", callback_data="F1")

    E = types.InlineKeyboardButton(text ="USER (BFFF2)", callback_data="F2")

    M = types.InlineKeyboardButton('المطور', url='https://t.me/zy_42')

    mas.add(A,E,M)

    bot.send_message(message.chat.id, f"- welcom \n\n- Bot insta 🧑‍💻\n\n♻️ لوحة تحكم عمك هههههه ♨️",reply_markup=mas)


@bot.callback_query_handler(func=lambda call: True)
def masg(call):


	global nam

	if call.data =="zy_42":

		mas = types.InlineKeyboardMarkup(row_width=2)

		A = types.InlineKeyboardButton(text ="USER (BFFFL)", callback_data="F1")

		E = types.InlineKeyboardButton(text ="USER (BFFF2)", callback_data="F2")

		M = types.InlineKeyboardButton('المطور', url='https://t.me/zy_42')


		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="- welcom \n\n- Bot insta 🧑‍💻\n\n♻️ لوحة تحكم عمك هههههه ♨️",reply_markup=mas)

	elif call.data =="F1":

		ro = "_.qwertyuiopasdgfhjklzxcvbnm1234567890"
		u = ''
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(ro)for x in range(0)))
			ua = str(''.join(random.choice(ro)for x in range(6)))
			username = us + u + ua
			url = f'http://www.instagram.com/{username}/'
			headers = {
            'User-Agent': generate_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/emailsignup/',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7',}
			response = requests.get(url, headers=headers)
			if response == 404
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ ᴜѕᴇʀɴᴀᴍᴇ ᴛᴇʟᴇɢʀᴀᴍ  ✓\n────── • ✧✧ • ──────\n‹ ᴜѕᴇʀɴᴀᴍᴇ : @{username}\n────── • ✧✧ • ──────\n• @zy_42")

			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{username}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('المطور', url='https://t.me/zy_42')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)




	elif call.data =="F2":

		ro = "qwerty_u.iopasdfghjklzxcvbnm1234567890"
		u = ''
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(ro)for x in range(0)))
			ua = str(''.join(random.choice(ro)for x in range(5)))
			username = us + u + ua
			url = f'http://www.instagram.com/{username}/'
			headers = {
            'User-Agent': generate_user_agent(),
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/emailsignup/',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7'}
			response = requests.get(url, headers=headers)
			if response == 404
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ ᴜѕᴇʀɴᴀᴍᴇ ᴛᴇʟᴇɢʀᴀᴍ  ✓\n────── • ✧✧ • ──────\n‹ ᴜѕᴇʀɴᴀᴍᴇ : @{username}\n────── • ✧✧ • ──────\n• @zy_42")

			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}', callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{username}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('المطور', url='https://t.me/zy_42')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)


@server.route(f'/{BOT_TOKEN}', methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url='https://skorx.herokuapp.com/' + (BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 80)))