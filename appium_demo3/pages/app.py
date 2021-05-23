# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : app.py
from appium import webdriver
from ..config import config
from ..pages.base_page import BasePage
from ..pages.main_page import MainPage

cfg = config.COMMCFG
import logging

logging.basicConfig(level=logging.INFO)


class App(BasePage):
    def start(self):
        if self.driver == None:
            logging.info("init driver...")
            self.driver = webdriver.Remote(cfg.url, cfg.desired_caps)
        else:
            logging.info("reuse driver...")
            self.driver.launch_app()

        self.driver.implicitly_wait(15)
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()
        logging.info("retart app..")

    def close_app(self):
        self.driver.close_app()
        logging.info("app close..")

    def stop(self):
        self.driver.quit()
        logging.info("driver quit..")

    def goto_main(self):
        return MainPage(self.driver)
