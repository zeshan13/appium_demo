#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : clock_in_succeed_page.py
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from ..pages.base_page import BasePage


class ClockInSucceed(BasePage):
    def general_clock_in_succeed(self):
        try:
            # 页面提示“打卡已完成”
            self.find(MobileBy.XPATH, '//*[contains(@text,"打卡已完成")]')
        except NoSuchElementException:
            # 早退打卡
            self.find(MobileBy.XPATH, '//*[contains(@text,"你早退了")]')
            self.find(MobileBy.XPATH, '//*[contains(@text,"确认打卡")]').click()
            self.find(MobileBy.XPATH, '//*[contains(@text,"打卡已完成")]').click()
        else:
            return NoSuchElementException

    def outside_clock_in_succeed(self):
        # 页面提示“打卡成功“
        self.find(MobileBy.XPATH, '//*[contains(@text,"打卡成功")]')
