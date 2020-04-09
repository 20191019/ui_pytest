import pytest
from ObjectLayer.LoginPage import LoginPage
from SharingMethod.config import Config


@pytest.fixture(scope='function', autouse=True)
def login(driver):
    """BusinessLayer模块，每次执行方法后的启动和清理"""
    cf = Config(r'..\config.ini', 'k-occ_test')
    user_name3 = cf.split_txt('user_name')[2]
    password2 = cf.split_txt('password')[2]
    lg = LoginPage(driver, 10)
    lg.login(user_name3, password2)
    yield
    # 执行每个用例之后要清除一下cookie，
    # 否则你第一个账号登录之后，重新加载网址还是登录状态，无法测试后面的账号
    driver.delete_all_cookies()


