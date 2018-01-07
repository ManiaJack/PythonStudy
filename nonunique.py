#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'输入一个list，去除其中非重复的元素，返回一个不改变剩余元素顺序的list.'

__author__ = 'ManiaJack'


def non_unique(lis):
    # 提取唯一的元素和序列号进入字典
    unique_dict = {}
    non_unique_list = []
    for i in range(len(lis)):
        if lis[i] in non_unique_list:
            continue
        elif lis[i] in unique_dict:
            unique_dict.pop(lis[i])
            non_unique_list.append(lis[i])
        else:
            unique_dict[lis[i]] = i
    # 倒序唯一元素的序列号，从后往前删除元素
    for i in sorted(unique_dict.values(), reverse=True):
        lis.pop(i)
    return lis
