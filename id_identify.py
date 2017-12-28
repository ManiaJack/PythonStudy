#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'This is for ID identify'

__author__ = 'ManiaJack'


def id2code(s):
    def char2num(x):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[x]
    coe = {0: 7, 1: 9, 2: 10, 3: 5, 4: 8, 5: 4, 6: 2, 7: 1, 8: 6, 9: 3, 10: 7, 11: 9, 12: 10, 13: 5, 14: 8, 15: 4, 16: 2}
    sum_num = 0
    l = []
    for i in s[:17]:
        l.append(char2num(i))
    for i in range(17):
        sum_num = sum_num + coe[i] * l[i]
    return sum_num % 11


def id_identify(s):
    if len(s) != 18:
        return print('请输入18位身份证号')
    check_code = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}
    if check_code[id2code(s)] != s[-1].upper():
        print('请输入正确的身份证号！')
    else:
        print('True ID number. ')
        if int(s[16]) % 2 == 1:
            print('性别：男')
        else:
            print('性别：女')
        print('出生日期：%s年%s月%s日' % (s[6:10], s[10:12], s[12:14]))


if __name__ == '__main__':
    id_identify(input('请输入身份证号：'))
    import time
    time.sleep(5)
