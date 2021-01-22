#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/11/30 5:07 PM
# @Author: zhangzhihui.wisdom
# @File:sodaDrinkBottleExchange.py
import sys
from selenium import webdriver


def sodaDrinkBottleExchange(bottlesNumber):
    result = 0
    if bottlesNumber == 0:
        result = 0
    while bottlesNumber != 0:
        temp = bottlesNumber // 3
        result += temp
        bottlesNumber = bottlesNumber % 3 + temp
        if bottlesNumber < 3:
            break
    if bottlesNumber == 2:
        result += 1
    print(result)


if __name__ == '__main__':
    # print('Soda drink bottle exchange')
    # # method three
    #
    # # bottleOne = list(map(int, input().split(',')))
    # # print(bottleOne)
    # sodaDrinkNumber = int(input())
    # sodaDrinkBottleExchange(sodaDrinkNumber)
    # strings = list(input().split(' '))
    # if strings[-1] != ' ':
    #     print(len(strings[-1]))
    #     print(len(strings))

    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")

    # strings = input()
    # chars = input()
    # lists = list(strings)
    # print(lists)
    # number = 0
    # for i in lists:
    #     if i == chars:
    #         number += 1
    #   print(number)
