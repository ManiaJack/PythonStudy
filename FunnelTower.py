#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
输入符号数量与符号，画出漏斗形状如图：
********
 *****
  ***
   *
  ***
 *****
*******
用上尽可能多的符号，同时输出层数与剩余符号数。
"""

__author__ = 'ManiaJack'


import re


# 根据符号数量计算行数
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


# 根据行数和符号画出漏斗
def funnel_print(n, s):
    for x in range(n):
        f = ' ' * x + s * (2 * (n - x) - 1)
        print(f)
    for x in range(n - 1):
        f = ' ' * (n - x - 2) + s * (2 * x + 3)
        print(f)


# 识别符号数量和符号
def funnel_split(s):
    re_funnel = re.compile(r'^(-?[\d]+)\s*(.)+$')
    try:
        n = int(re_funnel.match(s).group(1))
        s = re_funnel.match(s).group(2)
        return [n, s]
    except AttributeError:
        raise AttributeError('输入格式错误，请输入数字+符号')


def funnel(s):
    x = funnel_split(s)
    fun_info = funnel_layer(x[0])
    funnel_print(fun_info[0], x[1])
    print('层数: %d, 剩余符号数: %d' % (fun_info[0], fun_info[1]))


if __name__ == '__main__':
    str_input = input('输入漏斗塔符号数及符号：\n')
    funnel(str_input)
