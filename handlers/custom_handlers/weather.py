from loader import bot
from states.route_date import UserRoute
from telebot.types import Message
from api.cities_api import data_base
from api.weather_api import weather


@bot.message_handler(commands=['survey', "Ввести город чтобы найти погоду"])
def survey(message: Message) -> None:
    bot.set_state(message.from_user.id, UserRoute.start_city, message.chat.id)
    bot.send_message(message.from_user.id, f'{message.from_user.username}, введи город, в котором хочешь узнать погоду')


@bot.message_handler(state=UserRoute.start_city)
def get_start_city(message: Message) -> None:
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['start_city'] = str(message.text)[:1].upper() + str(message.text)[1:]
    bot.send_message(message.from_user.id,
                     f"Спасибо, записал! Город - {data['start_city']}")
    from handlers.default_handlers import help
    try:
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data_cities = data_base(data['start_city'])

            result_way = weather(data_cities[0], data_cities[1])
            bot.send_message(message.from_user.id, result_way)

        bot.set_state(message.from_user.id, help, message.chat.id)
    except KeyError:
        bot.send_message(message.from_user.id, "Такого города не существует")
        bot.set_state(message.from_user.id, help, message.chat.id)
