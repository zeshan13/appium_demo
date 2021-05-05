#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : test_uiautomator.py

# pip install appium-python-client
from appium import webdriver
import time

class TestUiAutomator:
    def setup(self):
        des_caps = {
            "platformName": "android",
            "deviceName": "Huawei Mate30",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": "True",
            "unicodeKeyboard":"True",
            "resetKeyboard":"True"
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_check_alibaba(self):
        # 定位、点击搜索框
        # el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        # resourceId("com.xueqiu.android:id/tv_search")
        el1 = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tv_search")')
        el1.click()
        # 输入搜索关键词
        # el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el2 = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/search_input_text")')
        el2.send_keys("阿里巴巴")
        #点击搜索到的词条
        # Xpath定位
        # el3 = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
        el3 = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/name").text("阿里巴巴")')
        el3.click()
        # 点击阿里巴巴，进入股票页面
        # Xpath定位
        # el4 = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']")
        # el4 = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/stockName").text("阿里巴巴")')
        # 通过搜索结果列表框定位其儿子节点中text为“阿里巴巴”的元素
        el4 = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/ll_stock_result_view").childSelector(text("阿里巴巴"))')
        el4.click()
        # 获取当前股价
        # el5 = self.driver.find_element_by_id("com.xueqiu.android:id/stock_current_price")
        el5 = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/stock_current_price")')
        print("阿里巴巴当前股价为：%s"% str(el5.text))
        # 判断阿里巴巴股价是否大于200
        assert float(el5.text) > 200


    def test_scroll_to_article(self):
        time.sleep(1)
        # 滚动匹配包含"财经"的文本，并点击
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).'
            'instance(0)).scrollIntoView(new UiSelector().textContains("财经").'
            'instance(0))').click()














