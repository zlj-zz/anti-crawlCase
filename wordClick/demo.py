#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
__author__ = 'zachary'
"""
File Name: demo.py
Created Time: 2020-04-11 11:42:57
Last Modified: 
"""

import re
from selenium import webdriver
from parsel import Selector

url = 'http://www.porters.vip/captcha/clicks.html'

browser = webdriver.Firefox(executable_path='../geckodriver')
browser.get(url)
sel = Selector(browser.page_source)
# get verify requirement
require = sel.css('#divTips::text').get()
# print(require)
target = re.findall('“(.)”', require)
# print(target)

