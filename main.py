from random import choice, randint
import telebot


bot = telebot.TeleBot("8093504012:AAFQ8EV5cuYTnKQpns_39VG3cyGlcvXpVjA")

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(
        message.chat.id,
        "👋 Привет! Я бот. Вот что я умею:\n\n"
        "/coin — Подбросить монетку\n"
        "/dice — Бросить кубик\n"
        "/joke — Рассказать шутку\n"
        "/quote — Мудрая цитата\n"
        "/fact — Интересный факт\n"
        "/weather — Погода (в разработке)")
    
@bot.message_handler(commands=['coin'])
def coin_handler(message):
    result = choice(["ОРЕЛ", "РЕШКА"])
    bot.reply_to(message, f"🪙 Выпало: {result}")


@bot.message_handler(commands=['dice'])
def dice_handler(message):
    number = randint(1, 6)
    bot.reply_to(message, f"🎲 Выпало: {number}")


@bot.message_handler(commands=['joke'])
def joke_handler(message):
    jokes = [
        "Почему программисты путают Хэллоуин и Рождество? Потому что 31 Oct = 25 Dec.",
        "— Пап, а кто такой баг? — Не мешай, сынок, я тут с мамой разбираюсь.",
        "У программиста две проблемы: кэш и нейминг. И еще три: off-by-one ошибки."
    ]
    bot.reply_to(message, choice(jokes))


@bot.message_handler(commands=['quote'])
def quote_handler(message):
    quotes = [
        "«Будь изменением, которое хочешь видеть в мире.» — Махатма Ганди",
        "«Делай или не делай. Не пробуй.» — Йода",
        "«Чем больше я тренируюсь, тем удачливее я становлюсь.» — Гэри Плейер"
    ]
    bot.reply_to(message, choice(quotes))


@bot.message_handler(commands=['fact'])
def fact_handler(message):
    facts = [
        "🐙 Осьминог имеет три сердца и синюю кровь.",
        "⚡ Молния в 5 раз горячее поверхности Солнца.",
        "🌍 Земля вращается со скоростью примерно 1670 км/ч."
    ]
    bot.reply_to(message, choice(facts))

@bot.message_handler(commands=['weather'])
def weather_handler(message):
    bot.reply_to(message, "🌤 Погода пока не подключена. В будущем добавим настоящий прогноз!")


print("Бот запущен...")
bot.polling()
