# coding=utf-8
from SharingMethod.BasePage import BasePage
from SharingMethod.config import Config


class ShopNavigationPage(BasePage):
    """
    导航
    """
    cf = Config(r'..\DataLayer\ShopElementData.ini', '导航')
    shop1, shop2 = cf.split_txt('店铺')
    commodity_management1, commodity_management2 = cf.split_txt('店铺管理')
    commodity_information1, commodity_information2 = cf.split_txt('商品信息')

    def click_shop(self):
        """
        点击“店铺”
        :return:
        """
        self.click(ShopNavigationPage.shop1, ShopNavigationPage.shop2)

    def click_commodity_management(self):
        """
        点击“商品管理”
        :return:
        """
        self.click(ShopNavigationPage.commodity_management1, ShopNavigationPage.commodity_management2)

    def click_commodity_information(self):
        """
        点击“商品信息”
        :return:
        """
        self.click(ShopNavigationPage.commodity_information1, ShopNavigationPage.commodity_information2)


class NewCommodityClassificationPage(ShopNavigationPage):
    """
    商品分类
    """
    cf = Config(r'..\DataLayer\ShopElementData.ini', '商品分类')
    all_categories1, all_categories2 = cf.split_txt('全部分类')
    newly_added1, newly_added2 = cf.split_txt('新增')
    commodity_type_name1, commodity_type_name2 = cf.split_txt('商品类型名称')
    i_determine1, i_determine2 = cf.split_txt('新增_确定')
    i_cancel1, i_cancel2 = cf.split_txt('新增_取消')
    i_x1, i_x2 = cf.split_txt('新增_x')
    modify1, modify2 = cf.split_txt('修改')
    department_store1, department_store2 = cf.split_txt('分类_百货')
    delete1, delete2 = cf.split_txt('分类_厨具')
    kitchen_utensils1, kitchen_utensils2 = cf.split_txt('新名称')
    new_name1, new_name2 = cf.split_txt('修改_确定')
    u_determine1, u_determine2 = cf.split_txt('修改_取消')
    u_cancel1, u_cancel2 = cf.split_txt('修改_x')
    u_x1, u_x2 = cf.split_txt('删除')
    d_determine1, d_determine2 = cf.split_txt('删除_确定')
    d_cancel1, d_cancel2 = cf.split_txt('删除_取消')
    d_x1, d_x2 = cf.split_txt('删除_x')

    def click_all_categories(self):
        """
        点击“全部分类”
        :return:
        """
        self.click(NewCommodityClassificationPage.all_categories1, NewCommodityClassificationPage.all_categories2)

    def click_newly_added(self):
        """
        点击“新增”
        :return:
        """
        self.element_to_be_clickable(NewCommodityClassificationPage.newly_added1, NewCommodityClassificationPage.newly_added2)

    def send_keys_commodity_type_name(self, commodity_type_name):
        """
        输入“商品类型名称”
        :param commodity_type_name:商品类型名称
        :return:
        """
        self.send_keys(NewCommodityClassificationPage.commodity_type_name1, NewCommodityClassificationPage.commodity_type_name2, commodity_type_name)

    def click_determine(self):
        """
        点击新增中的“确定”
        :return:
        """
        self.click(NewCommodityClassificationPage.i_determine1, NewCommodityClassificationPage.i_determine2)

    def click_cancel(self):
        """
        点击新增中的“取消”
        :return:
        """
        self.click(NewCommodityClassificationPage.i_cancel1, NewCommodityClassificationPage.i_cancel2)

    def click_x(self):
        """
        点击新增中的“x”
        :return:
        """
        self.click(NewCommodityClassificationPage.i_x1, NewCommodityClassificationPage.i_x1)

    def click_modify(self):
        """
        点击“修改”
        :return:
        """
        self.click(NewCommodityClassificationPage.modify1, NewCommodityClassificationPage.modify2)

    def click_department_store(self):
        """
        点击“百货”分类（第2个分类）
        :return:
        """
        self.click(NewCommodityClassificationPage.department_store1, NewCommodityClassificationPage.department_store2)

    def click_delete(self):
        """
        点击“删除”
        :return:
        """
        self.click(NewCommodityClassificationPage.delete1, NewCommodityClassificationPage.delete2)

    def click_kitchen_utensils(self):
        """
        点击“厨具”分类（第3个分类）
        :return:
        """
        self.click(NewCommodityClassificationPage.kitchen_utensils1, NewCommodityClassificationPage.kitchen_utensils2)

    def send_keys_new_name(self, new_name):
        """
        输入“新名称”
        :param new_name: 新名称
        :return:
        """
        self.send_keys(NewCommodityClassificationPage.new_name1, NewCommodityClassificationPage.new_name2, new_name)

    def click_u_determine(self):
        """
        点击修改中“确定”
        :return:
        """
        self.click(NewCommodityClassificationPage.u_determine1, NewCommodityClassificationPage.u_determine2)

    def click_u_cancel(self):
        """
        点击修改中“取消”
        :return:
        """
        self.click(NewCommodityClassificationPage.u_cancel1, NewCommodityClassificationPage.u_cancel2)

    def click_u_x(self):
        """
        点击修改中“x”
        :return:
        """
        self.click(NewCommodityClassificationPage.u_x1, NewCommodityClassificationPage.u_x1)

    def click_d_determine(self):
        """
        点击删除中“确定”
        :return:
        """
        self.click(NewCommodityClassificationPage.d_determine1, NewCommodityClassificationPage.d_determine2)

    def click_d_cancel(self):
        """
        点击删除中“取消”
        :return:
        """
        self.click(NewCommodityClassificationPage.d_cancel1, NewCommodityClassificationPage.d_cancel2)

    def click_d_x(self):
        """
        点击删除中“x”
        :return:
        """
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
    t.click_newly_added()
    t.send_keys_commodity_type_name('11111')
    t.click_determine()
    sleep(10)
    t.quit()