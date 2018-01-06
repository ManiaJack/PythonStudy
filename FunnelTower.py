#!/usr/bin/env python3
# -*- coding:utf-8 -*-

r"Let's play a Funnel Tower!"

__author__ = 'ManiaJack'


import re


def funnel_layer(n):
    if n > 1000 or n <= 0:
        raise ValueError('Numbers have to be 1~1000')
    if n == 1:
        return [1, 0]
    n = n - 1
    x = 1
    while n >= 4 * x + 2:
        n = n - 4 * x - 2
        x = x + 1
    return [x, n]


def funnel_print(n, s):
    for x in range(n):
        f = ' ' * x + s * (2 * (n - x) - 1)
        print(f)
    for x in range(n - 1):
        f = ' ' * (n - x - 2) + s * (2 * x + 3)
        print(f)


def funnel_split(s):
    re_funnel = re.compile(r'^([\d]+)\s*(.+)$')
    try:
        n = int(re_funnel.match(s).group(1))
        s = re_funnel.match(s).group(2)
    except AttributeError:
        print('输入格式错误')
        return funnel(input('请重新输入：'))
    return [n, s]


def funnel(s):
    x = funnel_split(s)
    try:
        fun_info = funnel_layer(x[0])
    except ValueError as e:
        print('ValueError:', e)
        return funnel(input('请重新输入：'))
    funnel_print(fun_info[0], x[1])
    print('层数: %d, 剩余符号数: %d' % (fun_info[0], fun_info[1]))


if __name__ == '__main__':
    str_input = input('输入漏斗塔符号数及符号。\n：')
    funnel(str_input)
