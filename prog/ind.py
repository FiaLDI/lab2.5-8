#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    # Колличество винчестеров.
    COUNT_OF_VIN = 22
    
    list_of_turple = [tuple(map(int, input("Введите стоимость и вес через пробел: ").split())) for i in range(COUNT_OF_VIN)]

    # Искомая соимость
    value = int(input("Введите стоимость "))

    # Поиск винчестеров с стоимостью больше s
    list_of_rezult = [i for i in list_of_turple if i[0] > value]
    print(list_of_rezult)