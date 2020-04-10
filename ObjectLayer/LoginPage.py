# coding=utf-8
from SharingMethod.BasePage import BasePage
from SharingMethod import config

# 登录
class 登录类(BasePage):

    # 获取配置文件数据
    cf = config.Config(r'..\config.ini', 'k-occ_test')
    url = cf.get_config('url')
    user_name1, user_name2, user_name3 = cf.split_txt('user_name')
    password1, password2, password3 = cf.split_txt('password')
    login_button1, login_button2 = cf.split_txt('login_button')


    def 登录(self, usrName, passWord):
        """
        正常登录
        """
        self.open_url(登录类.url)
        self.send_keys(登录类.user_name1, 登录类.user_name2, usrName)
        self.send_keys(登录类.password1, 登录类.password2, passWord)
        self.click(登录类.login_button1, 登录类.login_button2)


if __name__ == '__main__':
    from selenium import webdriver
    bs = webdriver.Chrome()
    login = 登录类(bs, 10)
    login.登录('13666666666', '666666')