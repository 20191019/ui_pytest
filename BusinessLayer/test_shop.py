# -*- coding:utf-8 -*-
import pytest
from LogicLayer.Shop import *
from time import sleep
from SharingMethod.config import Config


"""
测试:商品分类
"""
class TestCommoditylassification(object):


    @pytest.mark.run(order=1)
    @pytest.mark.P1  # 用例分类
    def test_new_product_category_1(self, driver):
        """正常新增"""
        cf = Config('..\DataLayer\ShopTestData.ini', 'test_new_product_category_1')
        ts = NewCommodityClassification(driver, 10)
        ts.new_product_category('厨具')

    def test_modify_commodity_classification_1(self, driver):
        """正常修改"""
        cf = Config('..\DataLayer\ShopTestData.ini', 'test_new_product_category_1')
        ts = NewCommodityClassification(driver, 10)
        ts.modify_commodity_classification('调味品')

    def test_delete_product_category(self, driver):
        """正常删除"""
        cf = Config('..\DataLayer\ShopTestData.ini', 'test_new_product_category_1')
        ts = NewCommodityClassification(driver, 10)
        ts.delete_product_category()



if __name__ == '__main__':
    pytest.main("test_shop.py")