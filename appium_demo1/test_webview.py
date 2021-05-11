#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : test_webview.py
# pip install appium-python-client
from appium import webdriver
import time
from appium.webdriver.common.mobileby import MobileBy

class TestWebView:
    def setup(self):
        desired_caps = {
            "platformName": "android",
            "platformVersion": "7.1.2",
            "deviceName":"127.0.0.1:62001",
            "browserName":"Browser",
            "chromedriverExecutable":"F:\\chromedriver_win32\\chromedriver_win32\\chromedriver.exe",
            "chromeOptions": {"w3c": False},
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()


    def test_browser(self):
        self.driver.get("https://www.baidu.com/")
        print(self.driver.contexts) #['NATIVE_APP', 'CHROMIUM']
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(MobileBy.ID,"index-kw").send_keys("appium webview测试")
        self.driver.find_element(MobileBy.ID,"index-bn").click()
