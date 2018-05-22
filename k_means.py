#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''k_means'''

__author__ = 'ManiaJack'


import random


def dist_cal(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5


def random_center(points, k):
    centroids = random.sample(points, k)
    return centroids


def k_means(points, k, dist_means=dist_cal, create_cent=random_center):
    p_len = len(points)
    cluster_assment = [-1 for _ in range(k)]
    centroids = create_cent(points, k)
    cluster_changed = True
    while cluster_changed:
        cluster_changed = False
        for i in range(p_len):
            min_dist = float('inf')
            min_index = -1
            for j in range(k):
                dist_j_i = dist_means(points[i], centroids[j])
                if dist_j_i < min_dist:
                    min_dist = dist_j_i
                    min_index = j
            if cluster_assment[i] != min_index:
                cluster_changed = True
                cluster_assment[i] = min_index
        print(centroids)
        for cent in range(k):
            temp_points = [points[i] for i in range(p_len) if cluster_assment[i] == cent]
            centroids[cent] = [sum([p[0] for p in temp_points]) / len(temp_points),
                               sum([p[1] for p in temp_points]) / len(temp_points)]
    cluster_points = [[] for _ in range(k)]
    print(cluster_assment)
    for i in range(k):
        cluster_points[i] = sorted([points[j] for j in range(p_len) if cluster_assment[j] == i])
    return sorted(cluster_points, key=lambda x: x[0][0])
