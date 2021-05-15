#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : outside_clock_in_page.py
from appium.webdriver.common.mobileby import MobileBy
from ..pages.base_page import BasePage
from ..pages.clock_in_succeed_page import ClockInSucceed

class OutsideClockIn(BasePage):
    def goto_clock_in_succeed(self):
        # 点击【第n次打卡】
        self.find(MobileBy.XPATH, '//*[contains(@text,"次外出")]').click()
        return ClockInSucceed(self.driver)
