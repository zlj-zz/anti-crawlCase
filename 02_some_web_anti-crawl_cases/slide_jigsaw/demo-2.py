#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
__author__ = 'zachary'
"""
File Name: demo-2.py
Created Time: 2020-04-11 09:16:15
Last Modified: 
"""

from selenium import webdriver
from PIL import Image
from PIL import ImageChops

url = 'http://www.porters.vip/captcha/jigsawCanvas.html'
browser = webdriver.Firefox(executable_path='../geckodriver')
browser.get(url)
jigsawCircle = browser.find_element_by_css_selector('#jigsawCircle')
jigsawCanvas = browser.find_element_by_css_selector('#jigsawCanvas')
jigsawCanvas.screenshot('before.png')
# click block
action = webdriver.ActionChains(browser)
action.click_and_hold(jigsawCircle).perform()
# excute js hide radio
script = '''
var missblock = document.getElementById('missblock');
missblock.style['visibility'] = 'hidden';
'''
browser.execute_script(script)
jigsawCanvas.screenshot('after.png')
# open image
image_a = Image.open('after.png')
image_b = Image.open('before.png')
# compare differences to get coordinates
diff = ImageChops.difference(image_a, image_b)
diff_position = diff.getbbox()
print(diff_position)
# move block
position_x = diff_position[0]
action.move_by_offset(int(position_x) - 10, 0)
action.release().perform()
