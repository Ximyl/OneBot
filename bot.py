
import telebot
from telebot import types



bot = telebot.TeleBot(token)

@bot.message_handler(content_types =['text', 'contact'])
def main(message):
    if message.text == 'Поехали':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_main = types.KeyboardButton(text="Отправить местоположение", request_location=True)
        keyboard.add(button_main)
        bot.send_message(message.chat.id, "Привет! Нажми на кнопку и передай мне свое местоположение", reply_markup=keyboard)


def location(message):
    if message.location is not None:
        if (message.location.latitude > 55) and (message.location.latitude < 56) and (message.location.longitude > 82) and (message.location.latitude < 83):
            print(message.location)
            send = bot.send_message(message.chat.id, "latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))
        else:
            send = bot.send_message(message.chat.id, 'Неправильно')


bot.polling()