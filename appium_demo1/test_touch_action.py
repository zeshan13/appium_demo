#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : test_touch_action.py

# pip install appium-python-client
from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction

class TestTouchAction:
    def setup(self):
        descrip_cap = {
            "platformName": "android",
            "deviceName": "Huawei Mate30",
            "appPackage": "cn.kmob.screenfingermovelock",
            "appActivity": "com.samsung.ui.FlashActivity",
            "noReset": "True",
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", descrip_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_xueqiu(self):
        #点击开启手势密码
        el1 = self.driver.find_element_by_accessibility_id("手势密码锁")
        el1.click()
        # 绘制手势密码
        # 以下坐标试用 手机分辨率为540*960
        coordinate1 = (90,128)
        coordinate2 = (272,128)
        coordinate3 = (450,128)
        coordinate4 = (272,350)
        #分辨率 720*1280
        # coordinate1 = (120, 177)
        # coordinate2 = (357, 177)
        # coordinate3 = (602, 177)
        # coordinate4 = (357, 417)
        wait_time = 220 #单位为ms毫秒
        TouchAction(self.driver).press(x=coordinate1[0],y=coordinate1[1]).wait(wait_time)\
            .move_to(x=coordinate2[0],y=coordinate2[1]).wait(wait_time)\
            .move_to(x=coordinate3[0],y=coordinate3[1]).wait(wait_time)\
            .move_to(x=coordinate4[0],y=coordinate4[1]).wait(wait_time)\
            .release().perform()
        # 点击继续
        el2 = self.driver.find_element_by_id("cn.kmob.screenfingermovelock:id/btnTwo")
        el2.click()
        # 再次绘制绘制手势密码
        TouchAction(self.driver).press(x=coordinate1[0], y=coordinate1[1]).wait(wait_time) \
            .move_to(x=coordinate2[0], y=coordinate2[1]).wait(wait_time) \
            .move_to(x=coordinate3[0], y=coordinate3[1]).wait(wait_time) \
            .move_to(x=coordinate4[0], y=coordinate4[1]).wait(wait_time) \
            .release().perform()
        # 点击确认
        el3 = self.driver.find_element_by_id("cn.kmob.screenfingermovelock:id/btnTwo")
        el3.click()

