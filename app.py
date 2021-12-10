import telebot
from config import TOKEN


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(command=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Какую вы хотите пиццу? Большую или маленькую?'
    bot.reply_to(message, text)


bot.polling(none_stop=True)



from transitions import Machine