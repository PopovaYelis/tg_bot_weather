from telebot.handler_backends import State, StatesGroup


class UserRoute(StatesGroup):
    start_city = State()
