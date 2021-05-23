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
        # 随机生成name
        name = details.get_name()
        # 随机生成phone
        phone = details.get_phone_num()
        # 随机返回性别
        sex = random.choice(["男", "女"])
        # 最后一步在列表中添加的查找元素
        result = self.main.goto_cantacts().goto_add_member().goto_edit_personal_details().goto_add_member(name,
                                                                                                          phone,
                                                                                                          sex).goto_contacts().get_member(
            text=name)

        # 断言result为True即元素存在
        assert result == True
