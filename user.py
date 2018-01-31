# -*- coding: utf-8 -*-

TOKEN = '433340494:AAG_h5rM2oB_l3QOiNH_jlgskgd-QXePGD4'

import time
import telepot
from DBHelper import DBHelper
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup
from quote import writer, quote

bot = telepot.Bot(TOKEN)

# Instantiate a DBHelper object with the identifier 'db'
db = DBHelper()

reply_keyboard = ReplyKeyboardMarkup(keyboard = [['I want to reply'], ['Share my Thought'], ['Listen to a Thought']], one_time_keyboard = True, resize_keyboard = True)
reply_keyboard2 = ReplyKeyboardMarkup(keyboard = [['Like'], ['I want to reply'], ['Share my Thought'], ['Listen to another Thought'], ['Report this message as spam']], one_time_keyboard = True, resize_keyboard = True)
reply_keyboard3 = ReplyKeyboardMarkup(keyboard = [['Like'], ['Share my Thought'], ['Listen to another Thought']], one_time_keyboard = True, resize_keyboard = True)
reply_keyboard4 = ReplyKeyboardMarkup(keyboard = [['I want to reply',],['Share my Thought',],['Listen to another Thought',]], one_time_keyboard=True, resize_keyboard=True)
keyboard = ReplyKeyboardMarkup(keyboard = [['Share my Thought'], ['Listen to a Thought']], one_time_keyboard = True, resize_keyboard = True)
keyboard1 = ReplyKeyboardMarkup(keyboard = [['Share another Thought'], [ 'Listen to a Thought']], one_time_keyboard = True, resize_keyboard = True)
keyboard2 = ReplyKeyboardMarkup(keyboard = [['Confirm'], [ 'Enter again']], one_time_keyboard=True, resize_keyboard = True)

def conversation(msg):

    #Get information of the currently processing message，including the content， id of the sender and id of the message
    content_type, chat_type, chat_id = telepot.glance(msg)
    update = bot.getUpdates()
    content = msg['text']
    msgid = int(update[0]["update_id"])

    # When the user inputs '/start'，send the theme message
    if content_type == 'text' and content == '/start':
        bot.sendMessage(chat_id, text = 'Everyone has secrets. Sometimes we hope to tell it, while ending up with finding no one to tell. This time, through agony bot, you can exchange your secret with some strangers in an anonymous way. If you want, you can also reply to the sender, like his or her secret, or just listen. Hey! Please protect these little secrets for their owners, don’t tell anyone else! 24 hours, start exchanging from now!',reply_markup = keyboard)
    # When the user presses 'Share my Thought' or 'Share another Thought', ask him to input the message that he wants to send
    elif content_type == 'text' and (content == 'Share my Thought' or content == 'Share another Thought'):
        bot.sendMessage(chat_id, text = 'Hey! Welcome to today’s agony aunt! Please send your message. You will receive a little gift from us once you confirm sending the message :D')
    # When the user presses 'Listen to a Thought' or 'Listen to another Thought', retrieve a random message sent by other users from the database and send it to him，store this message receiving record in the database as well
    elif content_type == 'text' and (content == 'Listen to a Thought' or content == 'Listen to another Thought'):
        result = db.get_message(chat_id)
        db.add_reply(result[0], "", result[2], result[1], chat_id)
        bot.sendMessage(chat_id, text = result[0], reply_markup = reply_keyboard2)
    # When the user presses 'I want to reply', ask him to input his reply to the received message
    elif content_type == 'text' and content == 'I want to reply':
        bot.sendMessage(chat_id, 'Hey! Please enter your comment! It will be posted to the original sender! Hope you two could become friends or just remain strangers :D')
    # When the user presses 'Like', retrieve his last message receiving record from the database, update the number of 'like' of the 'liked' message, inform the sender of the 'liked' message of the action and the total number of 'like' that message has got
    elif content_type == 'text' and content == 'Like':
        reply = db.get_reply(chat_id)
        db.increase_like(reply[2])
        num = db.get_like(reply[2])
        bot.sendMessage(reply[0], "Wow,some one has liked your message:\n" + reply[1])
        bot.sendMessage(reply[0], "This message has been liked " + str(num) + " times.", reply_markup = keyboard)
        bot.sendMessage(chat_id, "You've liked this message", reply_markup = reply_keyboard4)
    # When the user presses 'Report this message as spam', retrieve his last receiving record from the database, update the 'spamming state' of the reported message
    elif content_type == 'text' and content == 'Report this message as spam':
        reply = db.get_reply(chat_id)
        db.mark_as_spam(reply[2])
        bot.sendMessage(chat_id, "Thanks for your report, our administer will look into this", reply_markup = keyboard1)
    # When the user presses 'Confirm', tell him that his message has been successfully shared
    elif content_type == 'text' and content == 'Confirm':
        bot.sendMessage(chat_id, "Receive! Exchanging in progress! Please wait :D\nToday\'s quote for you:\n %s\n %s" % (quote, writer), reply_markup = keyboard1)
    # When the user presses 'Enter again', delete his last message sharing record from the database, ask him to enter the message again
    elif content_type == 'text' and content == 'Enter again':
        lastid = db.last_sent_message(chat_id)
        db.delete_message(lastid)
        bot.sendMessage(chat_id, "Sure, please enter your message again.")
    # To deal with the stage of the conversation when user doesn't input from the keyboard
    else:
        # Retrieve the user's last input from the data and store it as the variable last_message
        last_message = db.get_last_message(chat_id)
        # If the user's last input is 'Share my Thought' or 'Share another Thought' or 'Enter again', store this message sharing record in the database
        if last_message == 'Share my Thought' or  last_message == 'Share another Thought' or  last_message == 'Enter again':
            db.add_message(content, chat_id, msgid)
            bot.sendMessage(chat_id, 'Please confirm to share this message :D', reply_markup = keyboard2)
        # If the user's last input is 'I want to reply', retrieve his last message receiving record from the database, send the reply to the sender of the corresponding original message
        if last_message == 'I want to reply':
            reply = db.get_reply(chat_id)
            bot.sendMessage(reply[0], "Some one has just replied your message:\n" + reply[1])
            bot.sendMessage(reply[0], "The reply is:\n"+content,reply_markup = keyboard)
            bot.sendMessage(chat_id, 'Your reply message has been sent. Thank you!!!', reply_markup = reply_keyboard3)
    # Store this user-input record in the database
    db.add_log(content,chat_id, msgid)
        
MessageLoop(bot, conversation).run_as_thread()

while 1:
    time.sleep(10)


















