# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver


class BasePage(object):
    """
    selenium的二次封装
    """
    def __init__(self, driver, outTime=30):

        self.driver = driver
        self.outTime = outTime
        self.byDic = {
            'id': By.ID,
            'name': By.NAME,
            'class_name': By.CLASS_NAME,
            'xpath': By.XPATH,
            'link_text': By.LINK_TEXT
        }

    def open_url(self, url):
        """
        打开浏览器
        :param url: 网址
        :return:
        """
        self.driver.get(url)
        self.driver.maximize_window()


    def find_element(self, by, element):
        """
        封装显性等待
        检查元素是否可以点击，等待时间为10s
        :param txt: 定位方法
        :param element: 元素
        :return:
        """
        try:
            et =  WebDriverWait(self.driver, self.outTime).until(lambda x : x.find_element(by, element))
        except Exception as e:
            print('定位：{0}\n没有找到元素:{1}'.format(by, element))
            self.driver.quit()
            raise e
        else:
            return et

    def element_to_be_clickable(self, by, element):
        """
        判断元素是否可以点击
        :param by: 定位方式
        :param element: 元素
        :return:
        """
        if by.lower() in self.byDic:
            try:
                print(self.byDic[by])
                et = WebDriverWait(self.driver, self.outTime).until(ec.element_to_be_clickable((self.byDic[by], element)))
                et.click()
            except Exception:
                print('定位：{0}\n没有找到元素:{1}'.format(by, element))
                return False
            return et
        else:
            print('定位：{0}\n没有找到元素:{1}'.format(by, element))

    def get_text(self, by, element):
        """获取元素的文本信息"""
        et = self.find_element(by, element)
        return et.text


    def click(self, by, element):
        """点击"""
        try:
            et = self.find_element(by, element)
            if et:
                et.click()
        except:
            print('定位：{0}\n没有找到元素:{1}'.format(by, element))


    def send_keys(self, by, element, text):
        """输入数据，上传数据"""
        et = self.find_element(by, element)
        if et:
            et.clear()
            et.send_keys(text)
        else:
            print('定位：{0}\n没有找到元素:{1}'.format(by, element))

    def clear(self, by, element):
        """输入数据，上传数据"""
        et = self.find_element(by, element)
        if et:
            et.clear()
        else:
            print('定位：{0}\n没有找到元素:{1}'.format(by, element))


    def refresh(self):
        """刷新浏览器"""
        self.driver.refresh()

    def quit(self):
        self.driver.quit()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    a = BasePage(driver)
    a.open_url('http://xb.rfidstar.cn/k-occ/views/login.jsp')
    a.send_keys('name', 'loginName','13666666666' )
    a.send_keys('name', 'loginPassWord', '666666')
    a.element_to_be_clickable('id', 'loginBtn')
    cc = a.get_text('id', 'user_name')
    print(cc)