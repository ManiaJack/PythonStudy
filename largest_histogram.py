#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'根据输入的数组寻找最大的长方形'

__author__ = 'ManiaJack'


def largest_histogram(histo_list):
    _len = len(histo_list)
    largest = 0
    for i in range(_len):
        temp_largest = histo_list[i]
        top = histo_list[i]
        temp_i = i
        while temp_i + 1 < _len:
            temp_i += 1
            if histo_list[temp_i] < top:
                top = histo_list[temp_i]
            if top * (temp_i - i + 1) > temp_largest:
                temp_largest = top * (temp_i - i + 1)
        if temp_largest > largest:
            largest = temp_largest
    return largest
