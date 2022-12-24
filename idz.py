#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def func_show(func):
    def get_sq(**wh):
        x = 1
        for v in wh.values():
            x *= int(v)
        func(x)
    return get_sq


@func_show
def result(wh):
    print(f"Площадь прямоугольника: {wh}")


if __name__ == '__main__':
    result(width=4, height=6)
   
  

