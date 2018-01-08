#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'判断国际象棋安全子'

__author__ = 'ManiaJack'


# 输入棋子坐标，返回保护子坐标
def safe_pawns_coor(position):
    if position[1] == '1':
        return False
    rank = str(int(position[1]) - 1)
    coor = 'abcdefgh'
    # 对于set()函数，要注意其同样可以作用于Iterable的字符串上，当保护子坐标只有一个时，必须返回Tuple或者List.
    if position[0] == 'a':
        return ('b' + rank,)
    elif position[0] == 'h':
        return ('g' + rank,)
    else:
        for i in range(8):
            if coor[i] == position[0]:
                n = coor[i - 1] + rank, coor[i + 1] + rank
                return coor[i - 1] + rank, coor[i + 1] + rank


# 判断保护子坐标是否有棋子
def safe_pawns_count(positions, coors):
    if not coors:
        return False
    if set(coors) & positions:
        return True
    else:
        return False


# 对每一个棋子计算判断有保护子并计数
def safe_pawns(positions):
    count = 0
    for position in positions:
        if safe_pawns_count(positions, safe_pawns_coor(position)):
            count += 1
    return count
