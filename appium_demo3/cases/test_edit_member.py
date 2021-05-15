#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : test_edit_member.py
import random
from ..pages.app import App

class TestEditMember:
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.close_app()

    def teardown_class(self):
        self.app.stop()

    def test_edit_member(self):
        member_list = self.main.goto_cantacts().get_member_list()
        print(f"member_list\n{member_list}")
        before_name = member_list[0]
        after_name = before_name + "_edit_test"
        after_sex = random.choice(["男","女"])
        after_member_list = self.main.goto_cantacts().goto_persional_details(
            before_name).goto_more_personal_details().goto_edit_persional_details().goto_persinal_details(after_name,after_sex).goto_contacts().get_member_list()
        print(f"after_member_list\n{after_member_list}")
        assert after_name in after_member_list
