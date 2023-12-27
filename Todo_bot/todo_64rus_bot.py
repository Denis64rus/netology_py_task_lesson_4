# pip3 install --user pyTelegramBotAPI - команда для установки библиотеки
import telebot

token = "6956471931:AAF-X8LO8BdJYuEBlu7S31vasIrOzBR7dWI"

bot = telebot.TeleBot(token)

# декоратор для регистрации функции для обработки текста
@bot.message_handler(content_types=["text"])

# функция обработки сообщений
# мы отправляем сообщение и получаем его же обратно как ответ
def echo(message):
    bot.send_message(message.chat.id, message.text)

# постоянные запросы к серверу телеграм
bot.polling(none_stop=True)