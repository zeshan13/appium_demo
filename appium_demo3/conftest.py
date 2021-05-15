#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-22 12:16
# @Author  : zeshan
# @File    : conftest.py
import allure
import pytest
from .config import config
from typing import List

cfg = config.COMMCFG

def ptest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')