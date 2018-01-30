#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'最长重复字符'

__author__ = 'ManiaJack'


def repeat_inside(string):
    _len = len(string)
    length_max = 0
    for index1 in range(_len - 1):
        for index2 in range(index1 + 1, _len):
            # 发现相同字符，代表疑似重复字符串开始
            if string[index1] == string[index2]:
                base_length = index2 - index1
                # 剩余字符串长度小于如果疑似字符串长度，则跳过循环
                if _len - index2 < base_length:
                    continue
                # 疑似字符串重复数为n，疑似字符串内容为base_str
                n = 0
                base_str = string[index1:index2]
                # 当第n个字符串长度不超过字符串总长度
                while index2 + n * base_length <= _len:
                    # 判断第n个字符串是否和疑似字符串相同，若相同，则n加一。否则结束循环。
                    if string[index2 + n * base_length:index2 + (n + 1) * base_length] == base_str:
                        n += 1
                    else:
                        break
                # 如果n等于0，说明疑似字符串非重复，继续循环
                if n == 0:
                    continue
                # 字符串总长度为疑似字符串长度+重复字符串长度，大于原最大值时记录疑似字符串和最大长度
                length = (n + 1) * base_length
                if length > length_max:
                    length_max = length
                    max_str = string[index1:index2 + n * base_length]
    if length_max == 0:
        return ''
    return max_str
