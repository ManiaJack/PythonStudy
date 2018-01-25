#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'不使用"import", "sum", "for", "while", "reduce"写一个数组求和函数'

__author__ = 'ManiaJack'


def my_sum(num_list):
    _len = len(num_list)
    new_list = []
    if _len > 1:
        new_list.append(num_list[0] + num_list[1])
        new_list += num_list[2:]
        return my_sum(new_list)
    return num_list[0]
