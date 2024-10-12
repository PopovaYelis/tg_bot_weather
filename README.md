## Цель: разработать телеграмм бота
## Как пользоваться:
КОМАНДЫ:
___
>> /start - старт, бот поздоровается и расскажет, что умеет делать.
>
>> /help - помощь, расскажет какие у бота есть команды и что они делают.
> 
>> /survey - ввод информации где ищем погоду
> 
---

1. API 

## Для работы будет использован API 
 - https://ai-weather-by-meteosource.p.rapidapi.com/daily

Запрос для нахождения широты и долготы.
- <https://api.travelpayouts.com/data/ru/cities.json?>


### ЗАПРОС ДЛЯ ПОИСКА ПОГОДЫ В ГОРОД ПРИЛЕТА (ПОГОДА СЕГОДНЯШНЯЯ):

- ПРИМЕР ЗАПРОСА ДЛЯ НАХОЖДЕНИЯ ПОГОДЫ 
>
> url=https://ai-weather-by-meteosource.p.rapidapi.com/daily"
> 
> querystring = {"lat":"37.81021","lon":"-122.42282","language":"en","units":"auto"} 
> 
> headers = {"X-RapidAPI-Key": "КЛЮЧ", "X-RapidAPI-Host": "ai-weather-by-meteosource.p.rapidapi.com"
} 
> 
> response = requests.get(url, headers=headers, params=querystring)
### Пример результата запроса
>{'lat': '37.81021N', 'lon': '122.42282W', 'elevation': 0, 'units': 'us', 'daily': {'data': [{'day': '2024-03-30', 'weather': 'partly_sunny', 'icon': 4, 'summary': 'Cloudy changing to partly sunny by afternoon. Temperature 49/58 °F.', 'predictability': 1, 'temperature': 52.0, 'temperature_min': 49.3, 'temperature_max': 58.3, 'feels_like': 49.3, 'feels_like_min': 44.8, 'feels_like_max': 55.6, 'wind_chill': 49.3, 'wind_chill_min': 44.8, 'wind_chill_max': 56.0, 'dew_point': 45.2, 'dew_point_min': 43.4, 'dew_point_max': 47.9, 'wind': {'speed': 7.3, 'gusts': 17.9, 'dir': 'NE', 'angle': 50}, 'cloud_cover': 58, 'pressure': 29.64, 'precipitation': {'total': 0.06, 'type': 'rain'}, 'probability': {'precipitation': 20, 'storm': 0.0, 'freeze': 0.0}, 'ozone': 437.14, 'humidity': 77, 'visibility': 14.02}
> 
> 
> 


# Как запустить:
1. Установка библиотек (через IDE или терминал):
   1. pyTelegramBotAPI==4.16.1
   2. python-dotenv==0.21.1
2. Файл .env 
   - в файле .env.templates лежат два ключа: 1. Токен бота 2. Ключ для апи. Их обязательно нужно заполнить иначе не будет работать.
3. Запуск бота выполняется из файла main, как только нажимаем run, бот начинает работать и отвечать на команды
