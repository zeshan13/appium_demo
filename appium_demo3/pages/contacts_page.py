#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : contacts_page.py
from appium.webdriver.common.mobileby import MobileBy
from ..pages.base_page import BasePage
from ..pages.personal_details_page import PersonalDetails

class Contacts(BasePage):
    def goto_add_member(self):
        from appium_demo.appium_demo3.pages.add_member_page import AddMember
        # 点击【添加成员】
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).'
            'instance(0)).scrollIntoView(new UiSelector().text("添加成员").'
            'instance(0))').click()
        return AddMember(self.driver)

    def goto_persional_details(self, member_name):
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).'
            'instance(0)).scrollIntoView(new UiSelector().text("' + member_name + '").'
                                                                                  'instance(0))').click()
        # self.find(MobileBy.XPATH, '//*[@text="' + member_name + '"]').click()
        return PersonalDetails(self.driver)

    def get_member_list(self):
        elements_obj = self.finds(MobileBy.XPATH,
                                  '//*[@text="企业通讯录"]/../following-sibling::android.widget.RelativeLayout//android.widget.TextView')
        member_list = [i.text for i in elements_obj]
        return member_list
