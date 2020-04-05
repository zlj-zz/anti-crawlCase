#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
__author__ = 'zachary'
"""
File Name: SVG.py
Created Time: 2020-04-05 17:23:43
Last Modified: 
"""

from parsel import Selector
import requests
import re

if __name__ == "__main__":
    mappings = {
        'vhk08k': 0,
        'vhk6zl': 1,
        'vhk9or': 2,
        'vhkfln': 3,
        'vhkbvu': 4,
        'vhk84t': 5,
        'vhkvxd': 6,
        'vhkqsc': 7,
        'vhkjj4': 8,
        'vhk0fl': 9,
    }

    # url = ''
    # resp = requests.get(url)
    resp = open('./html/case.html', 'r').read()
    sel = Selector(resp)

    numbers = sel.css('.more>d').extract()
    reg = r'class="(.*?)"'
    phone = []
    for number in numbers:
        number_code = re.findall(reg, number)[0]
        if 'vhk' in number_code:
            phone.append(mappings[number_code])
    phone = ''.join([str(i) for i in phone])
    print(phone)
