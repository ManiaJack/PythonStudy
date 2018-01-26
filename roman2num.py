#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'罗马数字转为阿拉伯数字'

__author__ = 'ManiaJack'


def reverse_roman(roman):
    roman_dict1 = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9}
    roman_dict10 = {'X': 1, 'XX': 2, 'XXX': 3, 'XL': 4, 'L': 5, 'LX': 6, 'LXX': 7, 'LXXX': 8, 'XC': 9}
    roman_dict100 = {'C': 1, 'CC': 2, 'CCC': 3, 'CD': 4, 'D': 5, 'DC': 6, 'DCC': 7, 'DCCC': 8, 'CM': 9}
    num = 0
    # 先判断首位是否为M
    while len(roman) > 0:
        if roman[0] == 'M':
            num += 1000
            roman = roman[1:]
        else:
            break
    while len(roman) > 0:
        _len = len(roman)
        # 根据字典计算数值
        for i in range(_len, 0, -1):
            roman_str = roman[:i]
            if roman_str in roman_dict100:
                num += roman_dict100[roman_str] * 100
                roman = roman[i:]
                break
            elif roman_str in roman_dict10:
                num += roman_dict10[roman_str] * 10
                roman = roman[i:]
                break
            elif roman_str in roman_dict1:
                num += roman_dict1[roman_str]
                roman = roman[i:]
                break
    return num
