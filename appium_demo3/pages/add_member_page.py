#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : add_member_page.py
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from appium_demo.appium_demo3.pages.base_page import BasePage


class AddMember(BasePage):
    def goto_edit_personal_details(self):
        from appium_demo.appium_demo3.pages.edit_personal_details_page import EditPersonalDetails
        # 点击【手动输入添加】
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return EditPersonalDetails(self.driver)

    def goto_contacts(self):
        from appium_demo.appium_demo3.pages.contacts_page import Contacts
        # 点击返回
        locator = (MobileBy.ID, "com.tencent.wework:id/i63")
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(locator))
        self.find(MobileBy.ID, "com.tencent.wework:id/i63").click()
        return Contacts(self.driver)
