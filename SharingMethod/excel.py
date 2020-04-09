# -*- coding:utf-8 -*-
import xlrd
from SharingMethod import ReEncapsulation


def sing_le(route, worksheet, h, g):
    """
    根据输入的路径、工作表、行、第几个，获取指定数据
    :param route: 文件路径（str）
    :param worksheet: 工作表名称（str）
    :param h: 第几行（int）
    :param g: 第几个（int）
    :return: 指定单元格数据（list）
    """
    # 打开excel
    data = xlrd.open_workbook(route)
    # 通过名称获取工作表
    sheet = data.sheet_by_name(worksheet)
    # 获取指定数据
    a = sheet.cell(h, g).value
    list_b = ReEncapsulation.expected_results(a)
    return list_b


def specified_column(route, worksheet, whole_column):
    """
    根据输入的工作表、列，获取整列数据
    :param route: 文件路径（str）
    :param worksheet: 工作表名称（str）
    :param whole_column: 列数（int）
    :return:指定列数据（list）
    """
    route = r'D:\Downloads\消费流水2020-01-11 19_05_10.xls'
    # 打开excel
    data = xlrd.open_workbook(route)
    # 通过名称获取工作表
    sheet = data.sheet_by_name(worksheet)
    # 获取指定列所有数据
    a = sheet.col(whole_column)
    return a


def SpecifiedRow(route, worksheet, whole_line):
    """
    根据输入的路径、工作表、行数，获取整行数据
    :param route: 文件路径（str）
    :param worksheet: 工作表名称（str）
    :param whole_line: 行数（int）
    :return:指定行数据（list）
    """
    # 打开excel
    data = xlrd.open_workbook(route)
    # 通过名称获取工作表
    sheet = data.sheet_by_name(worksheet)
    # 获取整行数据
    a = sheet.row(whole_line)
    return a



