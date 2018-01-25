#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'0<num<4000, 阿拉伯数字-->罗马数字'

__author__ = 'ManiaJack'


def num2roman(num):
    roman_dict1 = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 0: ''}
    roman_dict10 = {1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC', 0: ''}
    roman_dict100 = {1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM', 0: ''}
    roman = ''
    while num >= 1000:
        roman += 'M'
        num -= 1000
    roman += roman_dict100[num // 100]
    roman += roman_dict10[num // 10 % 10]
    roman += roman_dict1[num % 10]
    return roman
