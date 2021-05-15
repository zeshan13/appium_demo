#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : member_details.py
from faker import Faker

class MemberDetails:
    def __init__(self):
        self.faker = Faker('zh-CN')

    def get_name(self):
        name = self.faker.name()
        return "test" + name

    def get_phone_num(self):
        phone_num = self.faker.phone_number()
        return phone_num


if __name__ == '__main__':
    details = MemberDetails()
    print(details.get_name())
    print(details.get_phone_num())
