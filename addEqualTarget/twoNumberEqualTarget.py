#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/22 11:52 PM
# @Author: wisdom
# @File:twoNumberEqualTarget.py

from typing import List


def twoNumberAddEqualTarget(lists: List, target: int) -> List:
    hashmap = {}
    for ind, num in enumerate(lists):
        hashmap[num] = ind
    print(hashmap)
    for i, num in enumerate(lists):
        j = hashmap.get(target - num)
        if j is not None and i != j:
            return [i, j]


if __name__ == '__main__':
    print('two number equal target')
    target = int(input())
    lists = list(map(int, input().split()))
    print(twoNumberAddEqualTarget(lists, target))

