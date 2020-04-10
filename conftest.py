# -*- coding:utf-8 -*-
from selenium import webdriver
import pytest
import html
from py._xmlgen import html
import os
_driver = None


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: xx测试中心")])
    prefix.extend([html.p("测试人员: 黄涛")])

# @pytest.mark.optionalhook
# def pytest_html_results_table_header(cells):
#     cells.insert(1, html.th('Description'))
#     cells.pop(-1)  # 删除link列
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_row(report, cells):
#     cells.insert(1, html.td(report.description))
#     cells.pop(-1)  # 删除link列


def pytest_configure(config):
    """
    添加、删除【测试环境】
    :param config:
    :return:
    """
    # 添加接口地址与项目名称
    config._metadata["项目名称"] = "xxxxx"
    # config._metadata['接口地址'] = 'https://www.cnblogs.com/linuxchao/'
    # 删除Java_Home
    config._metadata.pop("JAVA_HOME")
    # config._metadata.pop("Base URL")
    # config._metadata.pop("Capabilities")
    # config._metadata.pop("Driver")


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    用于web自动化的错误用例截屏
    不使用时，注释该方法
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    # 如果你生成的是web ui自动化测试，请把下面的代码注释打开，否则无法生成错误截图
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            dirpng = r'D:\py1\ui_pytest\TestReport\png' #截屏图片保存地址
            if os.path.exists(dirpng) and os.path.isdir(dirpng):
                pass
            else:
                os.mkdir(dirpng)
            file_name = dirpng + report.nodeid.replace("::", "_") + ".png"
            file_name1 = r'./png/' + report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name1
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
    report.description = str(item.function.__doc__)


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('用例描述'))


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))


@pytest.fixture(scope='session', autouse=True)  # 声明为fixture(测试准备/清理)方法
def driver():
    """
    用于web自动化的错误用例截屏
     不使用时，注释该方法
    :return:
    """
    try:
        global _driver
        _driver = webdriver.Chrome()  # setup部分
        yield _driver  # teardown部分
        _driver.quit()
    except:
        _driver.quit()


def _capture_screenshot(name):
    """
    截屏
    :param name:
    :return:
    """
    _driver.get_screenshot_as_file(name)