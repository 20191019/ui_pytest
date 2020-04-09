from ObjectLayer.ShopPage import *


"""
逻辑:商品分类
"""
class NewCommodityClassification(NewCommodityClassificationPage):


    def get_into(self):
        """
        进入"商品信息"
        :return:
        """
        # 1.点击"店铺"
        self.click_shop()
        # 2.点击"商品管理"
        self.click_commodity_management()
        # 3.点击"商品信息"
        self.click_commodity_information()

    def new_product_category(self, commodity_type_name):
        """
        新增"商品分类"
        :param commodity_type_name: 新增的商品类型名称
        :return:
        """
        self.get_into()
        # 1.点击"百货"
        self.click_department_store()
        # 2.点击"新增"
        self.click_newly_added()
        # 3."商品类型名称"输入数据
        self.send_keys_commodity_type_name(commodity_type_name)
        # 4.点击"确定"
        self.click_determine()

    def modify_commodity_classification(self, new_name):
        """
        修改"商品分类"
        :param new_name: 修改的商品类型名称
        :return:
        """
        self.get_into()
        # 1.点击"厨具"
        self.click_kitchen_utensils()
        # 2.点击"修改"
        self.click_modify()
        # 3.输入"新名称"
        self.send_keys_new_name(new_name)
        # 4.点击"确定"
        self.click_u_determine()

    def delete_product_category(self):
        """
        删除"商品分类"
        :return:
        """
        self.get_into()
        # 1.点击"厨具"
        self.click_kitchen_utensils()
        # 2.点击"修改"
        self.click_delete()
        # 4.点击"确定"
        self.click_d_determine()


if __name__ == '__main__':
    from selenium import webdriver
    from time import sleep
    bs = webdriver.Chrome()
    t = NewCommodityClassification(bs, 10)
    t.open_url('http://xb.rfidstar.cn/k-occ/views/login.jsp')
    t.send_keys('name', 'loginName', '13666666666')
    t.send_keys('name', 'loginPassWord', '666666')
    t.click('id', 'loginBtn')
    t.new_product_category('1111')
    sleep(10)







