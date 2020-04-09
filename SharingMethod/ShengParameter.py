# -*- coding=utf-8 -*-
import time
import random


def m_s():
    """生成时间：2020-03-06 10:12:55"""
    a = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    return a


def str_random(several_number):
    """
    整数生成方法
    :param several_number: 需要随机生成整数的个数（int）
    :return: 生成数（str）
    """
    while True:
        a1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ]
        # 随机从a1列表中获取20位数字
        a = random.sample(a1, several_number)
        if a[0] == '0':
            continue
        else:
            # 将列表转换成string
            cor = ''.join(a)
        return cor


def order():
    """生成订单号 时间戳+3位随机数+4位随机数"""
    a = int(time.time())  # 时间戳
    b = str_random(3)
    c = str_random(4)
    return str(a) + b + c

