#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : main_page.py
from appium.webdriver.common.mobileby import MobileBy
from ..pages.base_page import BasePage
from ..pages.contacts_page import Contacts
from ..pages.workbench_page import Workbench


class MainPage(BasePage):
    def goto_cantacts(self):
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return Contacts(self.driver)

    def goto_workbench(self):
        self.find(MobileBy.XPATH, "//*[@text='工作台']").click()
        return Workbench(self.driver)
