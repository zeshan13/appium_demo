#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : test_toast.py
# pip install appium-python-client
from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from appium.webdriver.common.mobileby import MobileBy

class TestXueQiu:
    def setup(self):
        des_caps = {
            "platformName": "android",
            "deviceName": "Huawei Mate30",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": "True",
            "unicodeKeyboard":"True",
            "resetKeyboard":"True",
            "automationName":"uiautomator2"
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_toast(self):
        # 点击【我的】
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='我的']").click()
        # 点击【手机号】登录
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_login_phone').click()
        # 输入手机号码
        self.driver.find_element_by_id('com.xueqiu.android:id/register_phone_number').send_keys("13800000000")
        # 点击【发送验证码】
        self.driver.find_element_by_id('com.xueqiu.android:id/register_code_text').click()
        # 等待toast元素加载
        locator = (MobileBy.XPATH,'//*[@text="验证码已发送"]')
        WebDriverWait(self.driver,30).until(expected_conditions.presence_of_element_located(locator))
        # # 打印当前页面元素树
        print(self.driver.page_source)
        # toast元素
        # <android.widget.Toast index="1" package="com.android.settings" class="android.widget.Toast" text="验证码已发送" checkable="false" checked="false" clickable="false" enabled="false" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][0,0]" displayed="true" />
        # 等待toast元素消失
        WebDriverWait(self.driver, 30).until_not(expected_conditions.presence_of_element_located(locator))
        # 定位"重新获取"验证码按钮，获取文案
        text = self.driver.find_element_by_id('com.xueqiu.android:id/register_code_text').text
        assert "重新获取" in text



