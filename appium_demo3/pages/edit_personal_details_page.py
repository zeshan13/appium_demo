#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : edit_personal_details_page.py
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from ..pages.base_page import BasePage


class EditPersonalDetails(BasePage):
    def goto_persinal_details(self, name, sex):
        from appium_demo.appium_demo3.pages.personal_details_page import PersonalDetails
        # 输入姓名
        self.find(MobileBy.XPATH,
                  "//*[contains(@text,'姓名')]/following-sibling::android.widget.EditText").send_keys(name)
        # 选择性别
        self.find(MobileBy.XPATH, "//*[contains(@text,'性别')]/..//android.widget.ImageView").click()
        # 选择性别
        locator = (MobileBy.XPATH, "//*[contains(@text,'" + sex + "')]")
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(locator))
        self.find(locator).click()
        # 点击【保存】
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()
        return PersonalDetails(self.driver)

    def goto_contacts(self):
        from appium_demo.appium_demo3.pages.contacts_page import Contacts
        self.find(MobileBy.XPATH, "//*[@text='删除成员']").click()
        self.find(MobileBy.XPATH, "//*[@text='确定']").click()
        return Contacts(self.driver)

    def goto_add_member(self, name, phone, sex):
        from appium_demo.appium_demo3.pages.add_member_page import AddMember
        # 输入姓名
        self.find(MobileBy.XPATH,
                  "//*[contains(@text,'姓名')]/following-sibling::android.widget.EditText").send_keys(name)
        # 选择性别
        self.find(MobileBy.XPATH, "//*[contains(@text,'性别')]/..//android.widget.ImageView").click()
        locator = (MobileBy.XPATH, "//*[contains(@text,'" + sex + "')]")
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(locator))
        # 选择性别
        self.find(MobileBy.XPATH, "//*[contains(@text,'" + sex + "')]").click()
        # 输入手机号码
        self.find(MobileBy.XPATH, "//*[contains(@text,'手机号')]/..//android.widget.EditText").send_keys(
            phone)
        # 点击取消【保存后自动发送邀请通知】
        self.find(MobileBy.ID, "com.tencent.wework:id/fco").click()
        # 点击【保存】
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()
        # 等待【添加成功】出现
        locator = (MobileBy.XPATH, '//*[@text="添加成功"]')
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(locator))
        return AddMember(self.driver)
