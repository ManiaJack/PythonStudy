#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'查找逗号分隔单词的两个字符串的相同词汇'

__author__ = 'ManiaJack'


# split, join, sorted的使用
def find_words(string1, string2):
    string1 = string1.split(',')
    string2 = string2.split(',')
    words = []
    for word in string1:
        if word in string2:
            words.append(word)
    return ','.join(sorted(words))
