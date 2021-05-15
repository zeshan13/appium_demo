#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : base_page.py
import logging
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level=logging.INFO)

class BasePage:
    def __init__(self, driver: webdriver = None):
        self.driver = driver

    def find(self, by, ele=None):
        if ele:
            ele_obj = self.driver.find_element(by, ele)
            logging.info("find element ele=%s", ele)
        else:
            ele_obj = self.driver.find_element(*by)
            logging.info("find element ele=%s", by[1])

        return ele_obj

    def finds(self, by, ele=None):
        if ele:
            ele_obj = self.driver.find_elements(by, ele)
            logging.info("find elements ele=%s", ele)
        else:
            ele_obj = self.driver.find_elements(*by)
            logging.info("find elements ele=%s", by[1])
        return ele_obj

