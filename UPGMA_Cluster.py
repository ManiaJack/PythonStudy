#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''UPGMA_Cluster'''

__author__ = 'ManiaJack'


def cluster_dist(cluster1, cluster2):
    len1 = len(cluster1)
    len2 = len(cluster2)
    dist_sum = 0
    for point1 in cluster1:
        for point2 in cluster2:
            dist_sum += point_dist(point1, point2)
    return dist_sum / (len1 * len2)


def point_dist(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5


def UPGMA_cluster(points, k):
    cluster_all = [[point] for point in points]
    while len(cluster_all) > k:
        c_len = len(cluster_all)
        min_dist = float('inf')
        for i in range(c_len):
            for j in range(i + 1, c_len):
                if i != j:
                    temp_dist = cluster_dist(cluster_all[i], cluster_all[j])
                    if temp_dist < min_dist:
                        min_index = [i, j]
        cluster_all[min_index[0]] += cluster_all[min_index[1]]
        cluster_all.pop(min_index[1])
    for i in range(k):
        cluster_all[i] = sorted(cluster_all[i], key=lambda x: x[0])
    return sorted(cluster_all, key=lambda x: x[0][0])
