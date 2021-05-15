#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : test_clock_in.py
from ..pages.app import App

class TestClockIn:
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.close_app()

    def teardown_class(self):
        self.app.stop()

    def test_general_clock_in(self):
        self.main.goto_workbench().goto_general_clock_in().goto_clock_in_succeed().general_clock_in_succeed()

    def test_outside_clock_in(self):
        self.main.goto_workbench().goto_general_clock_in().goto_ouside_clock_in().goto_clock_in_succeed().outside_clock_in_succedd()
