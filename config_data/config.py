import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env.templates")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
RAPID_API_KEY_FLIGHT = os.getenv("RAPID_API_KEY_FLIGHT")
RAPID_API_KEY_WEATHER = os.getenv("RAPID_API_KEY_WEATHER")
DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("survey", "Ввести город чтобы найти погоду"),
)
