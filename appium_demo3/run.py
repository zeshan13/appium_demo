#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : run.py
import os
from config import config

cfg = config.COMMCFG
if __name__ == '__main__':
    result = cfg.result_dir
    report = cfg.report_dir
    # os.system("python -m pytest")
    os.system("allure generate --clean " + result + "  --report-dir " + report)
