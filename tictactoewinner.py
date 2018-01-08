#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'判断井字游戏胜平负'

__author__ = 'ManiaJack'


def tic_tac_toe_winner(game_result):
    # 判断每一行是否相同
    for result in game_result:
        if result == 'X' * 3:
            return 'X'
        if result == 'O' * 3:
            return 'O'
    # 判断每一列是否相同
    for line in range(3):
        if game_result[0][line] == game_result[1][line] == game_result[2][line] == 'X':
            return 'X'
        if game_result[0][line] == game_result[1][line] == game_result[2][line] == 'O':
            return 'O'
    # 判断斜向是否相同
    if game_result[0][0] == game_result[1][1] == game_result[2][2] == 'X' or game_result[0][2] == game_result[1][1] == game_result[2][0] == 'X':
        return 'X'
    if game_result[0][0] == game_result[1][1] == game_result[2][2] == 'O' or game_result[0][2] == game_result[1][1] == game_result[2][0] == 'O':
        return 'O'
    return 'D'
# 1. 判定库有未完成的结果，所以需要指定相同结果是否为X或O
# 2. 变量名太长易导致行字符数超标
