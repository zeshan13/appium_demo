#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : test_del_member.py
from ..pages.app import App

class TestAddMember:
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.close_app()

    def teardown_class(self):
        self.app.stop()

    def test_del_member(self):
        member_list = self.main.goto_cantacts().get_member_list()
        name = member_list[0]
        print(f"member_list:\n{member_list}")
        after_member_list = self.main.goto_cantacts().goto_persional_details(
            name).goto_more_personal_details().goto_edit_persional_details().goto_contacts().get_member_list()
        print(f"after_member_list:\n{after_member_list}")
        assert name not in after_member_list
