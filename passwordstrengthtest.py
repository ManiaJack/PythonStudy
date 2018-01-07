#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'输入字符串[a-zA-Z0-9]+，大于等于十位包含大小写+数字则返回True，否则返回False'

__author__ = 'ManiaJack'


import re


def password_test(password):
    if len(password) < 10:
        return False
    reaz, reAZ, re09 = '.*[a-z]', '.*[A-Z]', '.*[0-9]'
    if re.match(reaz, password) and re.match(reAZ, password) and re.match(re09, password):
        return True
    else:
        return False
