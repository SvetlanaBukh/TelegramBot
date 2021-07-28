

if __name__ == '__main__':
    import telebot
    token = "1895147463:AAE7aBDL6O2qCzsJ_n-8aaVxhpX9iWsfyr8"

    bot = telebot.TeleBot(token)


    @bot.message_handler(content_types=["text"])
    def echo(m):
        bot.send_message(m.chat.id, m.text)


    bot.polling(none_stop=True)
