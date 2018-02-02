#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'矩阵转置'

__author__ = 'ManiaJack'


def transpose_matrix(matrix_a):
    _len_row = len(matrix_a)
    _len_col = len(matrix_a[0])
    at = [[] for _ in range(_len_col)]
    for i in range(_len_col):
        for j in range(_len_row):
            at[i].append(matrix_a[j][i])
    return at
