#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'排序算法'

__author__ = 'ManiaJack'


# 插入排序--直接插入排序
def straight_insert(ori_list):
    _len = len(ori_list)
    # 对第二个开始的数，向前比较
    for i in range(1, _len):
        # 若大于最后一个数，直接对下一个数进行对比
        if ori_list[i] < ori_list[i - 1]:
            temp = ori_list[i]
            j = i - 1
            # 一直向前比较，直到出现一个小于Temp值的数或者到达第一位
            while temp < ori_list[j] and j >= 0:
                ori_list[j + 1] = ori_list[j]
                j -= 1
            ori_list[j + 1] = temp
    return ori_list


# 希尔排序，分组插入排序
def shell_sort(ori_list):
    _len = len(ori_list)
    step = _len // 2
    while step > 0:
        for i in range(step, _len):
            if ori_list[i] < ori_list[i - step]:
                temp = ori_list[i]
                i -= step
                while temp < ori_list[i] and i >= 0:
                    ori_list[i + step] = ori_list[i]
                    i -= step
                ori_list[i + step] = temp
        step //= 2
    return ori_list


# 二元简单选择排序
def simple_selection_sort(ori_list):
    _len = len(ori_list)
    for i in range(_len // 2):
        _max = i
        _min = i
        for j in range(i, _len - i):
            if ori_list[j] > ori_list[_max]:
                _max = j
            if ori_list[j] < ori_list[_min]:
                _min = j
        ori_list[i], ori_list[_max] = ori_list[_max], ori_list[i]
        ori_list[-i - 1], ori_list[_min] = ori_list[_min], ori_list[-i - 1]
    return ori_list


# 堆排序（完全二叉树）
def max_heapify(ori_list, root, _len):  # 堆最大调整，使父节点的值大于子节点
    left, right = 2 * root + 1, 2 * root + 2
    larger = root
    if left < _len and ori_list[left] > ori_list[larger]:
        larger = left
    if right < _len and ori_list[right] > ori_list[larger]:
        larger = right
    if larger != root:
        ori_list[root], ori_list[larger] = ori_list[larger], ori_list[root]
        max_heapify(ori_list, larger, _len)


def build_max_heap(ori_list):
    _len = len(ori_list)
    for i in range((_len - 2) // 2, -1, -1):
        max_heapify(ori_list, i, _len)


def heap_sort(ori_list):
    build_max_heap(ori_list)
    _len = len(ori_list)
    for i in range(_len - 1, -1, -1):
        ori_list[0], ori_list[i] = ori_list[i], ori_list[0]
        max_heapify(ori_list, 0, i)
    return ori_list


# 冒泡
def bubble_sort(ori_list):
    _len = len(ori_list)
    for i in range(_len - 1):
        for j in range(_len - 1 - i):
            if ori_list[j] > ori_list[j + 1]:
                ori_list[j], ori_list[j + 1] = ori_list[j + 1], ori_list[j]
    return ori_list


# 冒泡改进，增加交换标识符，如果标识符为0，说明已完成排序，不需要继续判定
def bubble_sort2(ori_list):
    _len = len(ori_list)
    if_exchange = 1
    print(ori_list)
    for i in range(_len - 1):
        if if_exchange == 0:
            return ori_list
        if_exchange = 0
        for j in range(_len - i - 1):
            if ori_list[j] > ori_list[j + 1]:
                ori_list[j], ori_list[j + 1] = ori_list[j + 1], ori_list[j]
                if_exchange = 1
        print(ori_list)
    return ori_list


# 快速排序
def partition(ori_list, low, high):
    key = ori_list[low]
    while low < high:
        while low < high and ori_list[high] >= key:
            high -= 1
        ori_list[low] = ori_list[high]
        while low < high and ori_list[low] <= key:
            low += 1
        ori_list[high] = ori_list[low]
    ori_list[low] = key
    return low


def quick_sort(ori_list, low, high):
    if low < high:
        pk = partition(ori_list, low, high)
        quick_sort(ori_list, low, pk - 1)
        quick_sort(ori_list, pk + 1, high)
    return ori_list


# 归并排序
def merge(list_left, list_right):
    i, j = 0, 0
    m, n = len(list_left), len(list_right)
    merge_list = []
    while i < m and j < n:
        if list_left[i] < list_right[j]:
            merge_list.append(list_left[i])
            i += 1
        else:
            merge_list.append(list_right[j])
            j += 1
    merge_list += list_left[i:]
    merge_list += list_right[j:]
    return merge_list


def merge_sort(ori_list):
    _len = len(ori_list)
    if _len <= 1:
        return ori_list
    middle = _len // 2
    left_list = merge_sort(ori_list[:middle])
    right_list = merge_sort(ori_list[middle:])
    return merge(left_list, right_list)


# 基数排序
def radix_sort(ori_list, r):
    for k in range(r):
        s = [[] for _ in range(10)]
        for n in ori_list:
            s[n // 10**k % 10].append(n)
        ori_list = [n for bukket in s for n in bukket]
    return ori_list


if __name__ == '__main__':
    import time, random
    list1 = [straight_insert, shell_sort, simple_selection_sort, heap_sort, bubble_sort, merge_sort]
    for func in list1:
        origin_list = [random.randint(1, 9999) for _ in range(10000)]
        start_time = time.time()
        func(origin_list)
        print('方法%s用时%s' % (func.__name__, time.time() - start_time))
    origin_list = [random.randint(1, 9999) for _ in range(10000)]
    start_time = time.time()
    radix_sort(origin_list, 4)
    print('方法radix_sort用时%s' % (time.time() - start_time,))
