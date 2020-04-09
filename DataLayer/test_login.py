import pytest
from ObjectLayer.LoginPage import LoginPage
from SharingMethod.config import Config

"""登录的测试(应为BusinessLayer中设置了模块级的登录配置)"""
class TestLogin(object):

    cf = Config(r'D:\py1\ui_pytest\DataLayer\LoginTestData.ini','test_login_1')


    # 正常登录
    def test_login_001(self, driver):
        login = LoginPage(driver, 30)
        user_name3 = TestLogin.cf.split_txt('user_name')[2]
        password3 = TestLogin.cf.split_txt('password')[2]
        login.login(user_name3, password3)
        assert 1==1

    def test_login_002(self, driver):
        login = LoginPage(driver, 30)
        user_name3 = TestLogin.cf.split_txt('user_name')[2]
        password3 = TestLogin.cf.split_txt('password')[2]
        login.login(user_name3, password3)
        assert 1==2

if __name__ == '__main__':
    pytest.main('test_login.py')
