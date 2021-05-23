#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : workbench_page.py
from ..pages.base_page import BasePage
from ..pages.general_clock_in_page import GeneralClockIn


class Workbench(BasePage):
    def goto_general_clock_in(self):
        # 滚动寻找并点击【打卡】"
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).'
            'instance(0)).scrollIntoView(new UiSelector().text("打卡").'
            'instance(0))').click()

        return GeneralClockIn(self.driver)
