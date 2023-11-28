import telebot

bot = telebot.TeleBot('6397498879:AAGJlfUFauD4aNSlveucim8cDLVNbjKwWm0')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет!')


@bot.message_handler(commands=['bark'])
def main(message):
    bot.send_message(message.chat.id, '0_0')


@bot.message_handler(commands=['voice'])
def main(message):
    bot.send_message(message.chat.id, 'Мяу')


@bot.message_handler(commands=['show'])
def main(message):
    bot.send_message(message.chat.id, 'Это же [котики](https://youtu.be/-452p_9ESbM?si=4r7AoM7Q704iyKSL)',
                     parse_mode='Markdown')


@bot.message_handler(commands=['finish'])
def main(message):
    bot.send_message(message.chat.id, 'До связи!', parse_mode='Markdown')


bot.infinity_polling()