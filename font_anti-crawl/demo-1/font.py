#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
__author__ = 'zachary'
"""
File Name: font.py
Created Time: 2020-04-06 20:50:36
Last Modified: 
"""

from fontTools.ttLib import TTFont
import requests
import os

font_url = 'http://www.porters.vip/confusion/font/movie.woff'
content = requests.get(font_url).content
font_woff = './movie.woff'
if not os.path.exists(font_woff):
    with open(font_woff, 'wb') as f:
        f.write(content)
font = TTFont(font_woff)
font_xml = './movie.xml'
font.saveXML(font_xml)
