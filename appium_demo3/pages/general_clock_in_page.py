#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : general_clock_in_page.py
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from ..pages.base_page import BasePage
from ..pages.clock_in_succeed_page import ClockInSucceed
from ..pages.outside_clock_in_page import OutsideClockIn

class GeneralClockIn(BasePage):
    def goto_clock_in_succeed(self):
        try:
            self.find(MobileBy.XPATH, '//*[contains(@text,"上班打卡")]').click()
        except NoSuchElementException:
            #  已打卡，点击【更新】
            self.find(MobileBy.XPATH, '//*[contains(@text,"更新")]').click()
            self.find(MobileBy.XPATH, '//*[contains(@text,"更新下班卡")]').click()
        return ClockInSucceed(self.driver)

    def goto_ouside_clock_in(self):
        # 点击切换到【外出打卡】
        self.find(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        return OutsideClockIn(self.driver)
