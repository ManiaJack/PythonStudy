#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'缩进长数字'

__author__ = 'ManiaJack'


def friendly_number(num, base=1000, decimals=0, powers=('', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y'), suffix=''):
    num_neg = ''
    pow_ind = 0
    if num < 0:
        num = abs(num)
        num_neg = '-'
    # 小数点0位使用地板除，避免出现浮点数精确度问题
    if decimals == 0:
        while num >= base and pow_ind < len(powers) - 1:
            num = num // base
            pow_ind += 1
        return ''.join([num_neg, str(round(num)), powers[pow_ind], suffix])
    while num >= base and pow_ind < len(powers) - 1:
        num = num / base
        pow_ind += 1
    float_num = '%.' + str(decimals) + 'f'
    return ''.join([num_neg, float_num % num, powers[pow_ind], suffix])
