# coding=utf-8
from SharingMethod.BasePage import BasePage
from SharingMethod import config


class LoginPage(BasePage):
    # 获取配置文件数据
    cf = config.Config(r'..\config.ini', '全局登录配置')
    url = cf.get_config('网址')
    user_name1, user_name2, user_name3 = cf.split_txt('用户名输入框')
    password1, password2, password3 = cf.split_txt('密码输入框')
    login_button1, login_button2 = cf.split_txt('登录按钮')

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
