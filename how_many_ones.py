#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'十进制转为二进制，数有几个1'

__author__ = 'ManiaJack'


def how_many_ones(num):
    string = ''
    while num > 0:
        string += str(num % 2)
        num //= 2
    return string.count('1')
