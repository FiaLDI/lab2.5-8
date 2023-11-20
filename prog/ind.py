#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    # Колличество винчестеров.
    COUNT_OF_VIN = 22

    # Искомая соимость
    value = int(input("Введите стоимость "))

    list_of_turple = [
        tuple(map(int, input("Введите стоимость и вес через пробел: ").split())) 
        for _ in range(COUNT_OF_VIN)]

    # Поиск винчестеров с стоимостью больше s
    list_of_rezult = [
        weight_of_tuple 
        for (value_of_tuple, weight_of_tuple) in list_of_turple 
        if value_of_tuple > value]
    print(list_of_rezult)