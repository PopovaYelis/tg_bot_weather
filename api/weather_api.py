from config_data.config import RAPID_API_KEY_WEATHER
import requests
import json


def weather(lat_1, lon_1) -> str:
    """
    запрос к API прогноза погоды, для поиска погоды на сегодняшний день в городе прилета
    :param lat_1: широта
    :param lon_1: долгота
    :return: строка с погодными условиями в городе прилета
    """
    url = "https://ai-weather-by-meteosource.p.rapidapi.com/current"
    querystring = {"lat": lat_1, "lon": lon_1, "timezone": "auto", "language": "en", "units": "auto"}

    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY_WEATHER,
        "X-RapidAPI-Host": "ai-weather-by-meteosource.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    json_dict_weather = json.loads(response.text)
    result = (f"Температура в городе прилета: {json_dict_weather['current']['temperature']} Цельсия\n "
              f"Ощущается как: {json_dict_weather['current']['feels_like']} Цельсия\n"
              f"Влажность: {json_dict_weather['current']['humidity']}\n")
    return result