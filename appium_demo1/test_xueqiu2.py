#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : test_xueqiu2.py

# pip install appium-python-client
from appium import webdriver
import time

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
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_xueqiu(self):
        # 定位、点击搜索框
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el1.click()
        # 输入搜索关键词
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el2.send_keys("阿里巴巴")
        #点击搜索到的词条
        el3 = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
        el3.click()
        # 点击阿里巴巴，进入股票页面
        el4 = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']")
        el4.click()
        # 获取当前股价
        el5 = self.driver.find_element_by_id("com.xueqiu.android:id/stock_current_price")
        print("阿里巴巴当前股价为：%s"% str(el5.text))
        # 判断阿里巴巴股价是否大于200
        assert float(el5.text) > 200

