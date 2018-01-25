#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
把一个阿拉伯数字因式分解后重组，使所有位不超过十，输出最小的数值。
例：
20 = 2 * 2 * 5，可看作'225'。但是 20 = 4 * 5，45 < 225，所以输出45。
'''

__author__ = 'ManiaJack'


from functools import reduce


# 将数字分解为数组并返回。若有大于十的质数，则在数组为后一位。
def factory(num, fac_list):
    for i in range(9, 1, -1):
        if num % i == 0:
            fac_list.append(i)
            num /= i
            if num == 1:
                return sorted(fac_list)
            return factory(num, fac_list)
    fac_list.append(int(num))
    return fac_list


def num_factory(num):
    fac_list = factory(num, [])
    # 若最后一位为大于十的质数，直接返回0
    if fac_list[-1] >= 10:
        return 0
    return reduce(lambda x, y: 10 * x + y, fac_list)
