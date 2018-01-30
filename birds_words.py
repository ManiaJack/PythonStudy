#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'翻译鸟语'

__author__ = 'ManiaJack'


def translate(string):
    vowels = 'aeiouy'
    _len = len(string)
    index = 0
    words = ''
    while index < _len:
        words += string[index]
        if string[index] == ' ':
            index += 1
        elif string[index] in vowels:
            index += 3
        else:
            index += 2
    return words
