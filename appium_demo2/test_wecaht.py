#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : test_wechat.py

# pip install appium-python-client
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import time
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWeChat:
    @pytest.mark.skip()
    def test_wechat_clock_in(self,driver):
        # 定位、点击【工作台】
        driver.find_element(MobileBy.XPATH,"//*[@text='工作台']").click()

        #滚动寻找并点击【打卡】"
        driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).'
            'instance(0)).scrollIntoView(new UiSelector().text("打卡").'
            'instance(0))').click()

        # # 已打卡，点击【更新】
        driver.find_element(MobileBy.ID,"com.tencent.wework:id/ig6").click()
        # 更新下班卡
        driver.find_element(MobileBy.ID,"com.tencent.wework:id/auw").click()
        # 页面提示“打卡已完成”
        driver.find_element(MobileBy.XPATH,'//*[contains(@text,"打卡已完成")]')

        # 点击切换到【外出打卡】
        # driver.find_element(MobileBy.XPATH,"//*[@text='外出打卡']").click()
        # 点击【第n次打卡】
        # driver.find_element(MobileBy.XPATH,'//*[contains(@text,"次外出")]').click()
        # 页面提示“打卡成功“
        # driver.find_element(MobileBy.XPATH,'//*[contains(@text,"打卡成功")]')

    def test_add_member(self,driver):
        # 点击【通讯录】
        driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 点击【添加成员】
        driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        # 点击【手动输入添加】
        driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 输入姓名
        driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/following-sibling::android.widget.EditText").send_keys("小黄4")
        # 选择性别
        driver.find_element(MobileBy.XPATH, "//*[contains(@text,'性别')]/..//android.widget.ImageView").click()
        # 选择性别为【女】
        driver.find_element(MobileBy.XPATH, "//*[contains(@text,'女')]").click()
        # 输入手机号码
        driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机号')]/..//android.widget.EditText").send_keys("15809856742")
        # 点击取消【保存后自动发送邀请通知】
        driver.find_element(MobileBy.ID, "com.tencent.wework:id/fco").click()
        # 点击【保存】
        driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        # 等待【添加成功】出现
        locator = (MobileBy.XPATH, '//*[@text="添加成功"]')
        WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located(locator))