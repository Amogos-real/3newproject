import telebot

bot = telebot.TeleBot('7838725195:AAEBzRYsEfYDdcaWMTHaBQ8nJ8PZ5HxyQoQ')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я простой бот. Чем могу помочь?")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Я могу ответить на определённые сообщения. Попробуй отправить 'Привет', 'Как дела?'. Если хочешь чтобы создатель бота добавил какую то другую фразу просто напиши чтобы он добавил его в бота. Вот его юзер: @Amogussusy62")

@bot.message_handler(func=lambda message: message.text.lower() == 'привет')
def greet_user(message):
    bot.reply_to(message, "Привет! Рад тебя видеть!")

@bot.message_handler(func=lambda message: message.text.lower() == 'как дела?')
def ask_how_are_you(message):
    bot.reply_to(message, "У меня всё хорошо! Спасибо, что спросил!")

@bot.message_handler(func=lambda message: message.text.lower() == 'пока')
def say_goodbye(message):
    bot.reply_to(message, "До встречи! Хорошего дня!")


@bot.message_handler(func=lambda message: message.text.lower() == 'когда обновление?')
def when_update(message):
    bot.reply_to(message, "Я не знаю. Я просто же бот! Спроси @Amogussusy62 :)")

@bot.message_handler(func=lambda message: message.text.lower() == 'давай поиграем')
def lets_play(message):
    bot.reply_to(message, "Прости. Я не смогу поиграть потому что я просто обычный бот который сделан в Python.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Извини, я пока не знаю, как на это ответить. Попробуй другую команду или фразу.")

bot.polling()
