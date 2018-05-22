#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''Dice probability'''

__author__ = 'ManiaJack'


def target_ways(dice_number, sides, targets):
    dice_pour = [1] * dice_number
    ways = 0
    while dice_pour[-1] <= sides:
        result = 0
        for dice in dice_pour:
            result += dice
        if result == targets:
            ways += 1
        dice_pour[0] += 1
        for i in range(dice_number - 1):
            if dice_pour[i] > sides:
                dice_pour[i] = 1
                dice_pour[i + 1] += 1
    return ways


def total_ways(dice_number, sides):
    max_num = dice_number * sides
    ways_count = [[0] * max_num for _ in range(2)]
    dice_count = 1
    # 初始化第一个骰子
    for i in range(sides):
        ways_count[0][i] += 1
    flag = 0
    while dice_count < dice_number:
        dice_count += 1
        for i in range(max_num):
            ways_count[1-flag][i] = 0
            if i < sides:
                for j in range(i):
                    ways_count[1 - flag][i] += ways_count[flag][j]
            else:
                for j in range(sides):
                    ways_count[1 - flag][i] += ways_count[flag][i - j - 1]
        flag = 1 - flag
    return ways_count[flag]


def probability(dice_number, sides, targets):
    if dice_number * sides < targets or dice_number > targets:
        return 0
    return float('%.4f' % (total_ways(dice_number, sides)[targets - 1] / (sides ** dice_number)))


if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision


    assert (almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
