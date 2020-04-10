# coding=utf-8
from SharingMethod.BasePage import BasePage
from SharingMethod import config


class LoginPage(BasePage):
    # 获取配置文件数据
    cf = config.Config(r'..\config.ini', 'k-occ_test')
    url = cf.get_config('url')
    user_name1, user_name2, user_name3 = cf.split_txt('user_name')
    password1, password2, password3 = cf.split_txt('password')
    login_button1, login_button2 = cf.split_txt('login_button')

    def login(self, usr_name, pass_word):
        """
        正常登录
        """
        self.open_url(login.url)
        self.send_keys(login.user_name1, login.user_name2, usr_name)
        self.send_keys(login.password1, login.password2, pass_word)
        self.click(login.login_button1, login.login_button2)


if __name__ == '__main__':
    from selenium import webdriver
    bs = webdriver.Chrome()
    login = LoginPage(bs, 10)
    login.login('13666666666', '666666')