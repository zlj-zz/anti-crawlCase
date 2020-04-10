#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
__author__ = 'zachary'
"""
File Name: demo.py
Created Time: 2020-04-10 21:48:17
Last Modified: 
"""

from selenium import webdriver
import re
from parsel import Selector

url = 'http://www.porters.vip/captcha/jigsaw.html'
client = webdriver.Firefox(executable_path='../geckodriver')
client.get(url)
jigsawCircle = client.find_element_by_css_selector('#jigsawCircle')
action = webdriver.ActionChains(client)
action.click_and_hold(jigsawCircle).perform()
html = client.page_source

sel = Selector(html)
# get jigsaw and gap's css
mbk_style = sel.css('#missblock::attr("style")').get()
tbk_style = sel.css('#targetblock::attr("style")').get()
# function: get left param
extract = lambda x: ''.join(re.findall(r'left: (\d+|\d+.\d+)px', x))
# use extract, get left style of css
mbk_left = extract(mbk_style)
tbk_left = extract(tbk_style)
# calculate slide distance
distance = float(tbk_left) - float(mbk_left)

action.move_by_offset(distance, 0) # set sliding distance
action.release().perform() # lossen
