#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'判断字符串中的括号是否对应'

__author__ = 'ManiaJack'


def brackets(string):
    n_list = []
    # 使用字典判断对应
    n_dict = {'(': ')', '[': ']', '{': '}'}
    for n in string:
        if n == '[' or n == '(' or n == '{':
            n_list.append(n)
        if n == ')' or n == ']' or n == '}':
            if len(n_list) == 0:
                return False
            if n != n_dict[n_list[-1]]:
                return False
            n_list.pop()
    if len(n_list) != 0:
        return False
    return True
