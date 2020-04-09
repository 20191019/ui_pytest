import pytest


@pytest.fixture(scope='function')
def teardown_func(driver):
    """
    DataLayer模块，每次执行方法后的清理
    """
    yield
    #执行每个用例之后要清除一下cookie，
    #否则你第一个账号登录之后，重新加载网址还是登录状态，无法测试后面的账号
    driver.delete_all_cookies()