#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : config.py
import os

class ConstError(Exception): pass

class _const(object):
    def __setattr__(self, k, v):
        if k in self.__dict__:
            raise ConstError
        else:
            self.__dict__[k] = v


COMMCFG = _const()
COMMCFG.url = "http://127.0.0.1:4723/wd/hub"

COMMCFG.base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
COMMCFG.comm_dir = os.path.join(COMMCFG.base_dir,"comm")
COMMCFG.tools_dir = os.path.join(COMMCFG.base_dir,"tools")
COMMCFG.report_dir = os.path.join(COMMCFG.base_dir,"report")
COMMCFG.logs_dir = os.path.join(COMMCFG.base_dir,"logs")
COMMCFG.result_dir = os.path.join(COMMCFG.base_dir,"result")
COMMCFG.screenshots_dir = os.path.join(COMMCFG.base_dir,"screenshots")
COMMCFG.test_datas_dir = os.path.join(COMMCFG.base_dir,"test_datas")
COMMCFG.cookies_path = os.path.join(COMMCFG.comm_dir,"cookies.yaml")
COMMCFG.chromedriver_path = os.path.join(COMMCFG.tools_dir,"chromedriver.exe")

COMMCFG.desired_caps = {}
COMMCFG.desired_caps["platformName"] = "android"
COMMCFG.desired_caps["deviceName"] = "127.0.0.1:62001"
COMMCFG.desired_caps["appPackage"] = "com.tencent.wework"
COMMCFG.desired_caps["appActivity"] = ".launch.WwMainActivity"
COMMCFG.desired_caps["noReset"] = True
COMMCFG.desired_caps["udid"] = "127.0.0.1:62001"
COMMCFG.desired_caps["skipDeviceInitialization"] = True
COMMCFG.desired_caps["settings[waitForIdleTimeout]"] = 0


if __name__ == '__main__':
    print(COMMCFG.base_dir)
    print(COMMCFG.cookies_path)
