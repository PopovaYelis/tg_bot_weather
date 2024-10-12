import requests
import json

url = "https://api.travelpayouts.com/data/ru/cities.json?"
response = requests.get(url)
json_dict_city = json.loads(response.text)


def data_base(data) -> list:
    """
    Поиск в json словаре городов кодов аэропортов, широты, долготы
    :param data: словарь состояния пользователя(т.е. выбранный маршрут)
    :return: список с кодами аэропортов, широтой и долготой
    """
    lon_1, lat_1 = None, None
    city_name = data
    for city in json_dict_city:
        if city['name'] == city_name:
            lat_1 = city['coordinates']['lat']
            lon_1 = city['coordinates']['lon']
    data_cities = [lat_1, lon_1]
    if not data_cities[0]:
        raise KeyError
    return data_cities





