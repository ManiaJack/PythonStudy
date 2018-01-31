#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'奇怪又简单的大炮旋转=-='

__author__ = 'ManiaJack'


def all_ball_in(pipe_list, ball_list):
    for balls in ball_list:
        if pipe_list[balls] != 1:
            return False
    return True


def rotate(pipe_list, ball_list):
    pipe_len = len(pipe_list)
    rotate_list = []
    rotate_time = 0
    for _ in range(pipe_len):
        # 判断是否合适
        if all_ball_in(pipe_list, ball_list):
            rotate_list.append(rotate_time)
        # 旋转大炮
        pipe_list.insert(0, pipe_list[-1])
        pipe_list.pop()
        rotate_time += 1
    return rotate_list
