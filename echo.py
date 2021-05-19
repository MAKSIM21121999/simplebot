import telebot

bot = telebot.TeleBot('1744485725:AAGSyPz9wu9kg9EgWEL0abqImol0_2sJyr8')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()