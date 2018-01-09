#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'造轮子，min和max，第一版，纯函数'

__author__ = 'ManiaJack'


from collections import Iterable


# 对每一个元素根据key进行处理
def key_func(obj, key):
    return key(obj)


# 对字符串类型根据ascii进行最大排序
def max_str(string):
    temp = ord(string[0])
    for obj in string:
        if ord(obj) > temp:
            temp = ord(obj)
    return chr(temp)


# 对数字类型进行最大排序
def max_num(objs):
    temp = objs[0]
    for obj in objs:
        if obj > temp:
            temp = obj
    return temp


# 对字符串类型根据ascii进行最小排序
def min_str(string):
    temp = ord(string[0])
    for obj in string:
        if ord(obj) < temp:
            temp = ord(obj)
    return chr(temp)


# 对数字类型进行最小排序
def min_num(objs):
    temp = objs[0]
    for obj in objs:
        if obj < temp:
            temp = obj
    return temp


# max和min轮子，传入生成器/数列/字符串等，传入一个处理函数。所有注释与my_min相同
def my_max(*args, key=lambda x: x):
    objs = []
    # 如果是生成器/list/tuple/str等类型会导致只有一个元素，需要提取
    if len(args) == 1:
        args = args[0]
    # 对于生成器进行全内容提取
    if isinstance(args, Iterable):
        arg = []
        for obj in args:
            arg.append(obj)
        args = arg
    # 判断字符串or数字，字符串直接返回相应字母
    if isinstance(args, str):
        return max_str(args)
    for obj in args:
        objs.append(key_func(obj, key))
    return args[objs.index(max_num(objs))]


def my_min(*args, key=lambda x: x):
    objs = []
    if len(args) == 1:
        args = args[0]
    if isinstance(args, Iterable):
        arg = []
        for obj in args:
            arg.append(obj)
        args = arg
    if isinstance(args, str):
        return min_str(args)
    for obj in args:
        objs.append(key_func(obj, key))
    return args[objs.index(min_num(objs))]
