import telebot

from dz.config import TOKEN, keys
from dz.extensions import ConvertionException, CryproConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def helps(message: telebot.types.Message):
    text = ('Драсть! Для конвертации введите в одну строчку комманду форматом:\n<Имя валюты>\n \
<в какую перевести>\n <колличестов валюты>\n Увидеть список всех валют: /values')
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def helps(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Не корректные параметры запроса!')

        quote, base, amount = values
        total_base = CryproConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} = {total_base}'
        bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['photo', ])
def answer(message: telebot.types.Message):
    bot.reply_to(message, 'Я не просил твои Дикпики, Противный')


bot.polling(none_stop=True)
# Посмотреть отвыкшим глазом на Балтийскую волну.....
