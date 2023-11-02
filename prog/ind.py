#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":
    s = int(input())

    # Винчестеры.
    a = [(v, p) for v in range(40, 90, 10) for p in range(100, 500, 100)]

    # Поиск винчестеров с стоимостью больше s
    for por, item in enumerate(a):
        if item[0] > s:
            print(f"Винчестер: ({item[0]},{item[1]}) - {item[1]}")