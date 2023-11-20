#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    # Колличество винчестеров.
    N = 22
    
    Arr = []
    while N > 0:
        # Ввод стоимости
        x = int(input("Введите стоимость: "))
        # Ввод веса
        y = int(input("Введите вес: "))
        Arr.append((x,y))
        N -= 1

    # Искомая соимость
    s = int(input())

    # Поиск винчестеров с стоимостью больше s
    for item in Arr:
        if item[0] > s:
            print(f"Винчестер: ({item[0]},{item[1]}) - {item[1]}")