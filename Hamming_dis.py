#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'计算数字的汉明距离'

__author__ = 'ManiaJack'


# 将数字转化为二进制字符串
def dec2bin(num, bins=''):
    if num == 0:
        return ''.join(bins[::-1])
    return dec2bin(num // 2, bins + str(num % 2))


def hamming_dis(num1, num2):
    # 逆转字符串，补齐0
    num1 = dec2bin(num1)[::-1]
    num2 = dec2bin(num2)[::-1]
    hamming = 0
    if len(num1) >= len(num2):
        num2 += '0' * (len(num1) - len(num2))
    else:
        num1 += '0' * (len(num2) - len(num1))
    for n in range(len(num1)):
        if num1[n] != num2[n]:
            hamming += 1
    return hamming
