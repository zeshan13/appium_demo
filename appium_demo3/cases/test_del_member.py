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
        # 修改获取到通讯录列表，选择第一个成员进行删除
        name = member_list[0]
        # 最后一步查找被删除的元素是否在成员列表中
        result = self.main.goto_cantacts().goto_persional_details(
            name).goto_more_personal_details().goto_edit_persional_details().goto_contacts().get_member(text=name)

        assert result == False
