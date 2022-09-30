import telebot
from telebot import types
from pymongo import MongoClient
import time
from telegram import ParseMode

bot = telebot.TeleBot('455555555555555еееееееееееее')

cluster = MongoClient("mongodb+srv://ku56кр:reytr66i124q@clreter0.qa1ye.mongodb.net/?retryWrites=true&w=majority&ssl=true")

db = cluster['db_date']
collection = db['dateme']

first = ''
second = ''
third = ''
fourth = ''

@bot.message_handler(content_types=['text', 'photo'])

def startup(message):
	if collection.find_one({'_id' : message.from_user.id}) is None:
		collection.insert_one({'_id' : message.from_user.id})
	markup = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True, one_time_keyboard=True)
	markup.add("Да", "Нет")
	bot.send_message(message.from_user.id, 'Любишь ли ты Карелию?', reply_markup=markup)
	bot.send_photo(message.from_user.id, 'https://naekvatoremsk.ru/sites/default/files/0-13_77.jpg')
	bot.register_next_step_handler(message, night)

def night(message):
	first = message.text
	collection.update_one({"_id" : message.from_user.id},{ '$set' : {
		"first" :first
		}})
	if first == 'Нет':
		bot.send_message(message.from_user.id, 'Нет так нет. Есть как есть')
	else:
		markup = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True, one_time_keyboard=True)
		markup.add("Да", "Нет")
		bot.send_message(message.from_user.id, 'Ночи в лесу в палатке?', reply_markup=markup)
		bot.send_photo(message.from_user.id, 'http://iassets.ru/img/%D0%9A%D0%B0%D1%80%D1%82%D0%BE%D1%87%D0%BA%D0%B8/%D0%96%D0%B8%D0%BB%D0%B8%D1%89%D0%B0/31%20%D0%BF%D0%B0%D0%BB%D0%B0%D1%82%D0%BA%D0%B0.jpg')
		bot.register_next_step_handler(message, song)

def song(message):
	second = message.text
	collection.update_one({"_id" : message.from_user.id},{ '$set' : {
		"second" : second
		}})
	if second == 'Нет':
		bot.send_message(message.from_user.id, 'Нет так нет. Есть как есть')
	else:
		markup = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True, one_time_keyboard=True)
		markup.add("Да", "Нет")
		bot.send_message(message.from_user.id, 'Песнь под гитару летнюю?', reply_markup=markup)
		bot.send_photo(message.from_user.id, 'https://stihi.ru/pics/2021/03/30/3215.jpg')
		bot.register_next_step_handler(message, panama)

def panama(message):
	third = message.text
	collection.update_one({"_id" : message.from_user.id},{ '$set' : {
		"third" : third
		}})
	if third == 'Нет':
		bot.send_message(message.from_user.id, 'Нет так нет. Есть как есть')
	else:
		markup = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True, one_time_keyboard=True)
		markup.add("Да", "Нет")
		bot.send_message(message.from_user.id, 'Ах да! Серёжу в панамке?', reply_markup=markup)
		bot.send_photo(message.from_user.id, photo=open('C:\\Users\\ignat\\Pictures\\photo_2021-06-06_18-16-53.jpg', 'rb'))
		bot.register_next_step_handler(message, final)

def final(message):
	fourth = message.text
	collection.update_one({"_id" : message.from_user.id},{ '$set' : {
		"fourth" : fourth
		}})
	if fourth == 'Нет':
		bot.send_message(message.from_user.id, 'Нет так нет. Есть как есть')
	else:
		bot.send_message(message.from_user.id, 'Если здесь оказалась ты' + '\n' + 'То через две недели' + '\n' + 'Сделай паузу - скушай твикс' + '\n' + 'Ждут нас ели Карелии')





bot.polling(none_stop=True, interval=0)