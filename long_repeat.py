#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'返回字符串中连续出现的个数最多的相同字符数'

__author__ = 'ManiaJack'


def long_repeat(string):
    # 判断是否为空字符串
    if len(string) == 0:
        return 0
    num_temp = 1
    num = 1
    # 对比连续两个字符是否相等并计数
    for i in range(1, len(string)):
        if string[i - 1] == string[i]:
            num_temp += 1
        else:
            if num_temp > num:
                num = num_temp
            num_temp = 1
    if num > num_temp:
        return num
    return num_temp
