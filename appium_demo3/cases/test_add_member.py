#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : test_add_member.py
import random
from ..pages.app import App
from ..utils.member_details import MemberDetails

class TestAddMember:
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.close_app()

    def teardown_class(self):
        self.app.stop()

    # @pytest.mark.skip()
    def test_add_member(self):
        details = MemberDetails()
        name = details.get_name()
        phone = details.get_phone_num()
        sex = random.choice(["男", "女"])
        member_list = self.main.goto_cantacts().goto_add_member().goto_edit_personal_details().goto_add_member(name,
                                                                                                               phone,
                                                                                                               sex).goto_contacts().get_member_list()
        print("member_list:\n%s" % member_list)
        assert name in member_list
