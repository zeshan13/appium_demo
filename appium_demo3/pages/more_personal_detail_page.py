#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : more_personal_detail_page.py
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from ..pages.base_page import BasePage


class MorePersonalDetails(BasePage):
    def goto_edit_persional_details(self):
        from appium_demo.appium_demo3.pages.edit_personal_details_page import EditPersonalDetails
        self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/b_x" and @text="编辑成员"]').click()
        return EditPersonalDetails(self.driver)

    def goto_persional_details(self):
        from appium_demo.appium_demo3.pages.personal_details_page import PersonalDetails
        # 点击返回
        locator = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/i63"]')
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(locator))
        self.find(locator).click()
        return PersonalDetails(self.driver)
