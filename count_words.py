#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'传入字符串+关键词，匹配字符串中出现的关键词，返回出现的关键词的个数（无重复）。'

__author__ = 'ManiaJack'


import re


def count_words(strings, keywords):
    word_number = 0
    # 对每个关键词正则匹配并计数
    for words in keywords:
        re_rule = '.*' + words
        if re.match(re_rule, strings.lower()):
            word_number += 1
    return word_number
