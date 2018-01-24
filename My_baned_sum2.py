#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'不使用"import", "sum", "for", "while", "reduce"写一个数组求和函数'

__author__ = 'ManiaJack'


def my_sum(num_list):
    _len = len(num_list)
    if _len == 1:
        return num_list[0]
    num = num_list[0]
    num_list.pop(0)
    return num + my_sum(num_list)
