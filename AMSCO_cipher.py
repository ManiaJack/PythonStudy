#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'AMSCO cipher'

__author__ = 'ManiaJack'


def get_base_matrix(message_len, key_len):
    matrix_len = 0
    # 完整两行的数量
    matrix_len += message_len // (key_len * 3) * 2
    message_len -= key_len * 3 * matrix_len // 2
    # 判断是否有完整的第一行
    if message_len >= int(key_len * 1.5):
        matrix_len += 1
        message_len -= int(key_len * 1.5)
    # 如果还有多余字符，行数加一
    if message_len != 0:
        matrix_len += 1
    # 生成占位矩阵
    base_matrix = [[i for i in range(1, key_len + 1)] for _ in range(matrix_len)]
    for i in range(matrix_len):
        for j in range(key_len):
            base_matrix[i][j] = (i + j) % 2 + 1
    # 最后一行填充
    if message_len != 0:
        last_row_j = 0
        while message_len >= (matrix_len + last_row_j + 1) % 2 + 1:
            temp = (matrix_len + last_row_j + 1) % 2 + 1
            message_len -= temp
            base_matrix[matrix_len - 1][last_row_j] = temp
            last_row_j += 1
        if message_len != 0:
            base_matrix[matrix_len - 1][last_row_j] = 1
            last_row_j += 1
        for i in range(last_row_j, key_len):
            base_matrix[matrix_len - 1][i] = 0
    return base_matrix


def decode_amsco(message, key):
    key_len = len(str(key))
    message_len = len(message)
    base_matrix = get_base_matrix(message_len, key_len)
    message_index = 0
    matrix_len = len(base_matrix)
    # 将信息按照相应位数填入矩阵
    for key_num in range(1, 1 + key_len):
        key_index = str(key).index(str(key_num))
        for i in range(matrix_len):
            alpha_len = base_matrix[i][key_index]
            base_matrix[i][key_index] = message[message_index:message_index + alpha_len]
            message_index += alpha_len
    # 连接并返回
    for i in range(matrix_len):
        base_matrix[i] = ''.join(base_matrix[i])
    return ''.join(base_matrix)
