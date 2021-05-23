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
        # 修改获取到通讯录列表，选择第一个成员进行编辑
        before_name = member_list[0]
        # 修改后的name
        after_name = before_name + "_edit_test"
        # 随机返回性别
        after_sex = random.choice(["男", "女"])
        # 最后一步查找通讯录列表是否有after_name修改后的成员名称
        result = self.main.goto_cantacts().goto_persional_details(
            before_name).goto_more_personal_details().goto_edit_persional_details().goto_persinal_details(after_name,
                                                                                                          after_sex).goto_contacts().get_member(
            text=after_name)

        # 断言result为True即元素存在
        assert result == True
