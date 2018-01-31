# -*- coding: utf-8 -*-
TOKEN = '433340494:AAG_h5rM2oB_l3QOiNH_jlgskgd-QXePGD4'

import time
import telepot
from DBHelper import DBHelper
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup
from quote import writer, quote

# Send a specific message to a specific list of receivers
def message(receiver_list, message):
    bot = telepot.Bot(TOKEN)
    keyboard = ReplyKeyboardMarkup(keyboard = [['Share my Thought'], ['Listen to a Thought']], one_time_keyboard = True, resize_keyboard = True)
    for receiver in receiver_list:
        bot.sendMessage(receiver, message, reply_markup = keyboard)
# Send a specific announcement to all users
def publish(announcement):
    bot = telepot.Bot(TOKEN)
    db1 = DBHelper()
    keyboard = ReplyKeyboardMarkup(keyboard = [['Share my Thought'], ['Listen to a Thought']], one_time_keyboard = True, resize_keyboard = True)
    alluser = db1.get_all_user()
    for user in alluser:
        bot.sendMessage(user[0], announcement, reply_markup = keyboard)
