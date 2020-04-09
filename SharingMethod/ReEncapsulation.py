# -*- coding:utf-8 -*-
import re


def expected_results(s):
    """
    使用正则取等号后面的数据
    :param s:要取的字符串对象
    :return:结果列表
    """
    list_1 = re.findall(r'.*=(.*)', s, re.M)
    return list_1
