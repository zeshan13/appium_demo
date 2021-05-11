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
        des_caps = {
            "platformName": "android",
            "platformVersion": "7.1.2",
            "appPackage": "io.appium.android.apis",
            "appActivity": "io.appium.android.apis.ApiDemos",
            "noReset": "true",
            "deviceName":"127.0.0.1:62001",
            "chromedriverExecutable":"F:\\chromedriver_win32\\chromedriver_win32\\chromedriver.exe",
            "chromeOptions":{'w3c':False},
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_browser(self):
        self.driver.find_element_by_accessibility_id("Views").click()
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).'
            'instance(0)).scrollIntoView(new UiSelector().text("WebView").'
            'instance(0))').click()
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(MobileBy.ID,"i_am_a_textbox").clear()
        self.driver.find_element(MobileBy.ID,"i_am_a_textbox").send_keys("test 123")
        self.driver.find_element(MobileBy.ID,"i am a link").click()
