# coding=utf-8
from SharingMethod.BasePage import BasePage
from SharingMethod.config import Config

"""
导航:店铺
"""
class ShopNavigationPage(BasePage):
    cf = Config(r'D:\py1\ui_pytest\ObjectLayer\ShopElementData.ini', 'Navigation')
    shop1, shop2 = cf.split_txt('shop')  # 店铺
    commodity_management1, commodity_management2 = cf.split_txt('commodity_management')  # 店铺管理
    commodity_information1, commodity_information2 = cf.split_txt('commodity_information') # 商品信息

    # 1.点击“店铺”
    def click_shop(self):
        self.click(ShopNavigationPage.shop1, ShopNavigationPage.shop2)

    # 2.点击“商品管理”
    def click_commodity_management(self):
        self.click(ShopNavigationPage.commodity_management1, ShopNavigationPage.commodity_management2)

    # 3.点击“商品信息”
    def click_commodity_information(self):
        self.click(ShopNavigationPage.commodity_information1, ShopNavigationPage.commodity_information2)



"""
内容:商品分类
"""
class NewCommodityClassificationPage(ShopNavigationPage):
    cf = Config(r'D:\py1\ui_pytest\ObjectLayer\ShopElementData.ini', 'CommodityClassification')
    # 1.全部分类
    all_categories1, all_categories2 = cf.split_txt('all_categories')
    # 2.新增
    newly_added1, newly_added2 = cf.split_txt('newly_added')
    # 3.新增/商品类型名称
    commodity_type_name1, commodity_type_name2 = cf.split_txt('commodity_type_name')
    # 4.新增/确定
    i_determine1, i_determine2 = cf.split_txt('i_determine')
    # 5.新增/取消
    i_cancel1, i_cancel2 = cf.split_txt('i_cancel')
    # 3.新增/x
    i_x1, i_x2 = cf.split_txt('i_x')
    # 7.修改
    modify1, modify2 = cf.split_txt('modify')
    # 8.百货(第二个分类)
    department_store1, department_store2 = cf.split_txt('department_store')
    # 9.百货(第二个分类)
    delete1, delete2 = cf.split_txt('delete')
    # 10.厨具(第三个分类)
    kitchen_utensils1, kitchen_utensils2 = cf.split_txt('kitchen_utensils')
    # 11.修改/厨具/新名称
    new_name1, new_name2 = cf.split_txt('New_name')
    # 12.修改/确定
    u_determine1, u_determine2 = cf.split_txt('u_determine')
    # 13.修改/取消
    u_cancel1, u_cancel2 = cf.split_txt('u_cancel')
    # 14.修改/x
    u_x1, u_x2 = cf.split_txt('u_x')
    # 15.修改/确定
    d_determine1, d_determine2 = cf.split_txt('d_determine')
    # 16.修改/取消
    d_cancel1, d_cancel2 = cf.split_txt('d_cancel')
    # 17.新增/x
    d_x1, d_x2 = cf.split_txt('d_x')

    # 1.全部分类
    def click_all_categories(self):
        self.click(NewCommodityClassificationPage.all_categories1, NewCommodityClassificationPage.all_categories2)

    # 2.新增
    def click_newly_added(self):
        self.element_to_be_clickable(NewCommodityClassificationPage.newly_added1, NewCommodityClassificationPage.newly_added2)

    # 3.新增/商品类型名称
    def send_keys_commodity_type_name(self, commodity_type_name):
        self.send_keys(NewCommodityClassificationPage.commodity_type_name1, NewCommodityClassificationPage.commodity_type_name2, commodity_type_name)

    # 4.新增/确定
    def click_determine(self):
        self.click(NewCommodityClassificationPage.i_determine1, NewCommodityClassificationPage.i_determine2)

    # 5.新增/取消
    def click_cancel(self):
        self.click(NewCommodityClassificationPage.i_cancel1, NewCommodityClassificationPage.i_cancel2)

    # 6.新增/x
    def click_x(self):
        self.click(NewCommodityClassificationPage.i_x1, NewCommodityClassificationPage.i_x1)

    # 7.修改
    def click_modify(self):
        self.click(NewCommodityClassificationPage.modify1, NewCommodityClassificationPage.modify2)

    # 8.百货(第二个分类)
    def click_department_store(self):
        self.click(NewCommodityClassificationPage.department_store1, NewCommodityClassificationPage.department_store2)

    # 9.删除
    def click_delete(self):
        self.click(NewCommodityClassificationPage.delete1, NewCommodityClassificationPage.delete2)

    # 10.厨具(第三个分类)
    def click_kitchen_utensils(self):
        self.click(NewCommodityClassificationPage.kitchen_utensils1, NewCommodityClassificationPage.kitchen_utensils2)

    # 11.修改/厨具/新名称
    def send_keys_new_name(self, new_name):
        self.send_keys(NewCommodityClassificationPage.new_name1, NewCommodityClassificationPage.new_name2, new_name)

    # 12.修改/确定
    def click_u_determine(self):
        self.click(NewCommodityClassificationPage.u_determine1, NewCommodityClassificationPage.u_determine2)

    # 13.修改/取消
    def click_u_cancel(self):
        self.click(NewCommodityClassificationPage.u_cancel1, NewCommodityClassificationPage.u_cancel2)
    # 14.新增/x
    def click_u_x(self):
        self.click(NewCommodityClassificationPage.u_x1, NewCommodityClassificationPage.u_x1)

    # 15.删除/确定
    def click_d_determine(self):
        self.click(NewCommodityClassificationPage.d_determine1, NewCommodityClassificationPage.d_determine2)

    # 16.删除/取消
    def click_d_cancel(self):
        self.click(NewCommodityClassificationPage.d_cancel1, NewCommodityClassificationPage.d_cancel2)

    # 17.删除/x
    def click_d_x(self):
        self.click(NewCommodityClassificationPage.d_x1, NewCommodityClassificationPage.d_x2)


if __name__ == '__main__':
    from selenium import webdriver
    from time import sleep
    bs = webdriver.Chrome()
    t = NewCommodityClassificationPage(bs, 10)
    t.open_url('http://xb.rfidstar.cn/k-occ/views/login.jsp')
    t.send_keys('name', 'loginName', '13666666666')
    t.send_keys('name', 'loginPassWord', '666666')
    t.click('id', 'loginBtn')
    t.click_shop()
    t.click_commodity_management()
    t.click_commodity_information()
    t.click_all_categories()
    #sleep(1)
    t.click_newly_added()
    #sleep(2)
    t.send_keys_commodity_type_name('11111')
    t.click_determine()
    sleep(10)
    t.quit()