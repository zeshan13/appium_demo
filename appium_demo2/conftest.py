# pip install appium-python-client
import time
import allure
from appium import webdriver
import pytest
from appium_demo2.comm import config

from typing import List


cfg = config.COMMCFG
_driver = None


def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    '''
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅获取用例call且执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        # 添加allure报告截图
        if hasattr(_driver, "get_screenshot_as_png"):
            with allure.step('添加失败截图..'):
                allure.attach(_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
    # 参考：https://www.cnblogs.com/yoyoketang/p/12609871.html


@pytest.fixture(scope="session")
def driver():
    global _driver
    _driver = webdriver.Remote(cfg.url, cfg.desired_caps)
    _driver.implicitly_wait(10)
    yield _driver
    time.sleep(3)
    _driver.quit()








