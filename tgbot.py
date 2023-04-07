
import wikipediaapi
from googletrans import Translator
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = 'Token'

bot = telebot.TeleBot(TOKEN)
keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True)
wiki_wiki = wikipediaapi.Wikipedia('ru')
keyboard.add(KeyboardButton('start'))


e = "abcdefghijklmnopqrstuvwxyzZYXWVUTSRQPONMLKJIHGFEDCBA"
r = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Я Бот википедия. Только спроси и расскажу всё что ты захочешь ;)",
                     reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def search_function(message):
    try:
        page = en_or_ru(message.text)
        if page:
            bot.send_message(message.chat.id, page)
            
        else:
            raise Exception
    except:
        bot.send_message(message.chat.id, "Ничего не нашлось :( ")

def en_or_ru(text):
    for i in text:
        if i in e:
            wiki_wiki = wikipediaapi.Wikipedia("en")
            page_py = wiki_wiki.page(text)
            return page_py.text
            break
        elif i in r:
            wiki_wiki = wikipediaapi.Wikipedia("ru")
            page_py = wiki_wiki.page(text)
            return page_py.summary
            break
        

bot.infinity_polling()