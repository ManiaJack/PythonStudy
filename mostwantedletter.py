#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'输入只包含ASCII中字符的字符串，返回其中出现次数最多的字母，不分大小写，若出现重复字母，返回字母表中靠前的字母。'

__author__ = 'ManiaJack'


def most_wanted_letter(strings):
    letter_numbers = {}
    most_letter = []
    # 初始化字典
    alphabeta = 'abcdefghijklmnopqrstuvwxyz'
    for letters in alphabeta:
        letter_numbers[letters] = 0
    # 计数
    for letter in strings.lower():
        if letter in letter_numbers:
            letter_numbers[letter] += 1
    # 比较字母数量
    for k, v in letter_numbers.items():
        if v == max(letter_numbers.values()):
            most_letter.append(k)
    return sorted(most_letter)[0]  # 排序+返回
