#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'输入三角形三条边，输出三个角的角度'

__author__ = 'ManiaJack'


import math


def length2cos(a, b, c):
    cos = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
    degree = math.degrees(math.acos(cos))
    return round(degree)


def angle(a, b, c):
    length = sorted((a, b, c))
    degrees = []
    if length[0] + length[1] <= length[2]:
        return [0, 0, 0]
    degrees.append(length2cos(a, b, c))
    degrees.append(length2cos(b, c, a))
    degrees.append(length2cos(c, a, b))
    return sorted(degrees)
