#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'造轮子，min和max，第一版，纯函数'

__author__ = 'ManiaJack'


from collections import Iterable


def key_func(obj, key):
    return key(obj)


def max_str(string):
    temp = ord(string[0])
    for obj in string:
        if ord(obj) > temp:
            temp = ord(obj)
    return chr(temp)


def max_num(objs):
    temp = objs[0]
    for obj in objs:
        if obj > temp:
            temp = obj
    return temp


def min_str(string):
    temp = ord(string[0])
    for obj in string:
        if ord(obj) < temp:
            temp = ord(obj)
    return chr(temp)


def min_num(objs):
    temp = objs[0]
    for obj in objs:
        if obj < temp:
            temp = obj
    return temp


def my_max(*args, key=lambda x: x):
    objs = []
    if len(args) == 1:
        args = args[0]
    if isinstance(args, Iterable):
        arg = []
        for obj in args:
            arg.append(obj)
        args = arg
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
