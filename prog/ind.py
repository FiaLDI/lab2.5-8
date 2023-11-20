#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    # Колличество винчестеров.
    count_of_vin = 22
    
    list_of_turple = [tuple(map(int, input("Введите стоимость и вес через пробел: ").split())) for i in range(N)]

    # Искомая соимость
    value = int(input("Введите стоимость "))

    # Поиск винчестеров с стоимостью больше s
    rezult = [i for i in list_of_turple if i[0] > value]
    print(rezult)