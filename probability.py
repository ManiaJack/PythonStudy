#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'递归骰子点数概率算法'

__author__ = 'ManiaJack'


# 计算点数总的可能数
def possible_ways(dice_number, sides, target):
    if dice_number == 2:
        if target > sides:
            target = 2 * sides - target + 2
        if target % 2 == 1:
            return target // 2 * 2
        return target // 2 * 2 - 1
    ways = 0
    for dice_point in range(1, 1 + sides):
        if dice_number - 1 <= target - dice_point <= sides * (dice_number - 1):
            ways += possible_ways(dice_number - 1, sides, target - dice_point)
    return ways


def probability(dice_number, sides, target):
    if target > dice_number * sides or dice_number > target:
        return 0
    if dice_number == 1:
        return float('%.4f' % (1 / sides))
    all_possible = sides ** dice_number
    way_numbers = possible_ways(dice_number, sides, target)
    return float('%.4f' % (way_numbers / all_possible))


print(probability(1, 2, 0))