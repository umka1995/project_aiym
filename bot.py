# import telebot
# from pars import main as parse
# from pars import titles, list_img, descriptions
# from MyToken import token
# from telebot import types


# inline_keyboard = telebot.types.InlineKeyboardMarkup()
# buttons = {}
# for i in range(1, 6):
#     buttons['btn'+str(i)] = telebot.types.InlineKeyboardButton(str(i), callback_data=str(i))

#     inline_keyboard.add(buttons['btn'+str(i)])

# bot = telebot.TeleBot(token)


# @bot.message_handler(commands=['start'])
# def start(message):
#     chat_id = message.chat.id
#     bot.send_message(chat_id,  "Привет, о каком мероприятии вы хотите почитать?")
#     parse()
#     # bot.send_message(chat_id, titles)
#     count = 0
#     for title in titles:
#         count += 1
#         bot.send_message(chat_id, str(count)+ ' '+ title)
#     bot.send_message(chat_id, 'Какое мероприятие показать', reply_markup=inline_keyboard)


# @bot.callback_query_handler(func = lambda x: True)
# def inline(call):
#     chat_id = call.message.chat.id
#     income_keyboard = telebot.types.ReplyKeyboardMarkup()
#     btn1 = telebot.types.KeyboardButton('Description')
#     btn2 = telebot.types.KeyboardButton('Photo')
#     btn3 = telebot.types.KeyboardButton('Quit')
#     income_keyboard.add(btn1, btn2, btn3)
#     global msg
#     msg = bot.send_message(chat_id, 'Выбери', reply_markup=income_keyboard)
#     bot.register_next_step_handler(msg, get_category_income)
#     global info_index
#     info_index = int(call.data)-1


# def get_category_income(message):
#     chat_id = message.chat.id
#     entry_data = message.text

#     if entry_data == 'Description':
#         try:
#             bot.send_message(chat_id, descriptions[info_index])
#             msg = ''
#             bot.register_next_step_handler(msg, get_category_income)
#         except:
#             pass

#     elif entry_data == 'Photo':
#         try:
#             bot.send_message(chat_id, list_img[info_index])
#             msg = ''
#             bot.register_next_step_handler(msg, get_category_income)
#         except:
#             pass

#     elif entry_data == 'Quit':
#         bot.send_message(chat_id, 'Пока')


# if __name__ == '__main__':
#     bot.polling()


import telebot
from pars import main as parse
from pars import titles, list_img, descriptions
from MyToken import token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Привет, о каком мероприятии вы хотите почитать?")
    parse()
    for idx, title in enumerate(titles, start=1):
        bot.send_message(chat_id, f"{idx}. {title}")
    bot.send_message(chat_id, "Какое мероприятие показать?")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    try:
        event_index = int(message.text) - 1
        bot.send_message(chat_id, descriptions[event_index])
        bot.send_message(chat_id, list_img[event_index])
    except (ValueError, IndexError):
        bot.send_message(chat_id, "Неверный ввод. Пожалуйста, введите номер мероприятия.")

if __name__ == '__main__':
    bot.polling()
