#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'连续四个相同数字判定'

__author__ = 'ManiaJack'


def find_sequence(lists):
    _len = len(lists)
    for lines in lists:
        line_index = lists.index(lines)
        for _index in range(_len):
            # Horizontal
            if _index <= _len - 4:
                if lines[_index] == lines[_index + 1] == lines[_index + 2] == lines[_index + 3]:
                    return True
            # Vertical
            if line_index <= _len - 4:
                if lists[line_index][_index] == lists[line_index + 1][_index] == \
                        lists[line_index + 2][_index] == lists[line_index + 3][_index]:
                    return True
            # NW to SE
            if line_index <= _len - 4 and _index <= _len - 4:
                if lists[line_index][_index] == lists[line_index + 1][_index + 1] == \
                        lists[line_index + 2][_index + 2] == lists[line_index + 3][_index + 3]:
                    return True
            # SW to NE
            if line_index <= _len - 4 and _index >= 3:
                if lists[line_index][_index] == lists[line_index + 1][_index - 1] == \
                        lists[line_index + 2][_index - 2] == lists[line_index + 3][_index - 3]:
                    return True
    return False
