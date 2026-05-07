from src.api.aeroplane_api import AeroplanesAPI
from src.models.aeroplane import Aeroplane
from src.storage.json_saver import JSONSaver
from src.utils.utils import (
    filter_by_country,
    sort_by_altitude,
    get_top_n,
    filter_by_altitude_range,
)

def user_interaction():
    api = AeroplanesAPI()
    saver = JSONSaver()

    country = input("Введите страну: ")
    top_n = int(input("Топ N: "))
    countries_filter = input("Фильтр по странам регистрации: ").split()
    altitude_range = input("Диапазон высот (например 0-10000): ")

    raw_data = api.get_aeroplanes(country)

    planes = Aeroplane.cast_to_object_list(raw_data)

    # фильтрация
    if countries_filter:
        planes = filter_by_country(planes, countries_filter)

    planes = filter_by_altitude_range(planes, altitude_range)
    planes = sort_by_altitude(planes)

    top_planes = get_top_n(planes, top_n)

    for plane in top_planes:
        print(plane)
        saver.add(plane)

if __name__ == "__main__":
    user_interaction()