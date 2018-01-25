#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'寻找最长的回文字符'

__author__ = 'ManiaJack'


def longest_palindromic(string):
    _len = len(string)
    palindromic = []
    for i in range(_len - 1):
        for j in range(i+ 1, _len):
            if string[i] == string[j]:
                if string[i:j + 1] == string[i:j + 1][::-1]:
                    palindromic.append(string[i:j + 1])
    _len_p = len(palindromic)
    if _len_p == 0:
        return string[0]
    longest_i = 0
    for i in range(_len_p):
        if len(palindromic[i]) > len(palindromic[longest_i]):
            longest_i = i
    return palindromic[longest_i]
