#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : personal_details_page.py
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from ..pages.base_page import BasePage
from ..pages.more_personal_detail_page import MorePersonalDetails


class PersonalDetails(BasePage):
    def goto_more_personal_details(self):
        # 点击右上角三个点
        locator = (MobileBy.ID, 'com.tencent.wework:id/i6d')
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(locator))
        self.find(locator).click()
        return MorePersonalDetails(self.driver)

    def goto_contacts(self):
        from appium_demo.appium_demo3.pages.contacts_page import Contacts
        # 点击返回
        locator = (MobileBy.ID, 'com.tencent.wework:id/i63')
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(locator))
        self.find(locator).click()
        return Contacts(self.driver)
