from telebot.types import Message

from config_data.config import DEFAULT_COMMANDS
from loader import bot

@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    command = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
    text = "\n".join(command)
    bot.send_message(message.chat.id,
                     f"Привет, {message.from_user.full_name}! Я бот LISA, я могу найти какая погода в любом городе, \n{text}"
                     )

