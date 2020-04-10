# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver


class BasePage(object):
    """
    selenium的二次封装
    """

    def __init__(self, driver, out_time=15):

        self.driver = driver
        self.out_time = out_time
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
            et = WebDriverWait(self.driver, self.out_time).until(lambda x: x.find_element(by, element))
        except Exception as e:
            print('异常：{0}定位：{1}\n没有找到元素:{2}'.format(e, by, element))
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
                et = WebDriverWait(self.driver, self.out_time).until(ec.element_to_be_clickable((self.byDic[by], element)))
            except Exception as e:
                print('异常：{0}定位：{1}\n没有找到元素:{2}'.format(e, by, element))
            else:
                return et

    def frame_to_be_available_and_switch_to_it(self, frame):
        """
        判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False
        :param frame: 内嵌网页
        :return:
        """
        try:
            et = WebDriverWait(self.driver, self.out_time).until(
                ec.frame_to_be_available_and_switch_to_it(frame))
        except Exception as e:
            print('异常：{0}定位：{1}'.format(e, frame))
        else:
            return et

    def element_to_be_selected(self, element):
        """
        判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False
        :param element: 元素
        :return:
        """
        try:
            et = WebDriverWait(self.driver, self.out_time).until(
                ec.element_to_be_selected(element))
        except Exception as e:
            print('异常：{0}定位：{1}'.format(e, element))
        else:
            return et

    def current_window_handle(self):
        """
        获取当前窗口句柄
        :return:
        """
        current_window = self.driver.current_window_handle()
        return current_window

    def window_handles(self):
        """
        获取所有窗口句柄
        :return:
        """
        all_windows = self.driver.window_handles()
        return all_windows

    def get_text(self, by, element):
        """获取元素的文本信息"""
        et = self.find_element(by, element)
        return et.text

    def click(self, by, element):
        """点击"""
        et = self.element_to_be_clickable(by, element)
        et.click()

    def send_keys(self, by, element, text):
        """输入数据，上传数据"""
        et = self.element_to_be_clickable(by, element)
        et.clear()
        et.send_keys(text)

    def clear(self, by, element):
        """输入数据，上传数据"""
        et = self.element_to_be_clickable(by, element)
        et.clear()

    def refresh(self):
        """刷新浏览器"""
        self.driver.refresh()

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    a = BasePage(driver, 10)
    a.open_url('http://xb.rfidstar.cn/k-occ/views/login.jsp')
    a.send_keys('name', 'loginName', '13666666666')
    a.send_keys('name', 'loginPassWord', '666666')
    a.click('id', 'loginBtn')
    cc = a.get_text('id', 'user_name')
    print(cc)
