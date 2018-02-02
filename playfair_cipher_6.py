#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'6*6 普莱费厄密码(Playfair cipher)加密解密'

__author__ = 'ManiaJack'


# 文本准备
def text_prepare(string):
    string = string.lower()
    str_list = []
    for word in string:
        if word.isdigit() or word.isalpha():
            str_list.append(word)
    index = 0
    while index < len(str_list):
        if index == len(str_list) - 1:
            if str_list[-1] == 'z':
                str_list.append('x')
            else:
                str_list.append('z')
        if str_list[index] == str_list[index + 1]:
            if str_list[index] == 'x':
                str_list.insert(index + 1, 'z')
            else:
                str_list.insert(index + 1, 'x')
        index += 2
    return ''.join(str_list)


# 图表准备
def base_map(keyword):
    keyboard = 'abcdefghijklmnopqrstuvwxyz0123456789'
    key_map = ''
    for alpha in keyword:
        if alpha not in key_map:
            key_map += alpha
    for alpha in keyboard:
        if alpha not in key_map:
            key_map += alpha
    _map = []
    for i in range(6):
        _map.append(key_map[i * 6:i * 6 + 6])
    return _map


# 针对每个字符找对应坐标位置
def find_coord(_map, alpha):
    for i in _map:
        if alpha in i:
            return [_map.index(i), i.index(alpha)]


# 根据图表、文本进行加密或解密
def secret_word(_map, text, is_decode=False):
    _len = len(text)
    return_word = ''
    for i in range(_len // 2):
        coord1 = find_coord(_map, text[2 * i])
        coord2 = find_coord(_map, text[2 * i + 1])
        if coord1[0] == coord2[0]:
            if is_decode:
                coord1[1] -= 1
                coord2[1] -= 1
            elif coord1[1] == 5:
                coord1[1] = 0
                coord2[1] += 1
            elif coord2[1] == 5:
                coord2[1] = 0
                coord1[1] += 1
            else:
                coord1[1] += 1
                coord2[1] += 1
        elif coord1[1] == coord2[1]:
            if is_decode:
                coord1[0] -= 1
                coord2[0] -= 1
            elif coord1[0] == 5:
                coord1[0] = 0
                coord2[0] += 1
            elif coord2[0] == 5:
                coord1[0] += 1
                coord2[0] = 0
            else:
                coord1[0] += 1
                coord2[0] += 1
        else:
            coord1[1], coord2[1] = coord2[1], coord1[1]
        return_word += _map[coord1[0]][coord1[1]] + _map[coord2[0]][coord2[1]]
    return return_word


def encode(string, keyword):
    _map = base_map(keyword)
    text = text_prepare(string)
    return secret_word(_map, text)


def decode(string, keyword):
    _map = base_map(keyword)
    text = text_prepare(string)
    return secret_word(_map, text, is_decode=True)
