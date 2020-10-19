import re
import requests
import time
from lxml import etree

save_path = '~/Documents/'

headers = {
    'Host':
    'www.baidu.com',
    'User-Agent':
    'Mozilla/5.0 (X11; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0',
    'Accept':
    '*/*',
    'Accept-Language':
    'en-US,en;q=0.5',
    'X-Requested-With':
    'XMLHttpRequest',
    'Connection':
    'keep-alive',
    'Referer':
    'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E9%BE%99%E7%AC%A6%20%E4%B8%8B%E8%BD%BD&oq=%25E9%25BE%2599%25E7%25AC%25A6%2520%25E4%25B8%258B%25E8%25BD%25BD&rsv_pq=c73a3e87000254a8&rsv_t=26423%2BjJJBDy%2FhH%2FCJU9hAmuMbKbCIkbnr%2BUIQK3aBRt71xJRlUnOtP5iqE&rqlang=cn&rsv_dl=tb&rsv_enter=0&rsv_btype=t',
    'is_referer':
    'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E9%BE%99%E7%AC%A6%20%E4%B8%8B%E8%BD%BD&oq=requsets%2520https&rsv_pq=b793ec400001142b&rsv_t=566bNOXLrpw6uc1PZ8Olwt8M16V728piElQluc2o6knPadylZtUOVdbYZyI&rqlang=cn',
}

search_url = 'https://www.baidu.com/s?ie=utf-8&mod=1&isid=6A8BCCA443C96435&ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E9%BE%99%E7%AC%A6%20%E4%B8%8B%E8%BD%BD&oq=%25E9%25BE%2599%25E7%25AC%25A6%2520%25E4%25B8%258B%25E8%25BD%25BD&rsv_pq=c73a3e87000254a8&rsv_t=26423%2BjJJBDy%2FhH%2FCJU9hAmuMbKbCIkbnr%2BUIQK3aBRt71xJRlUnOtP5iqE&rqlang=cn&rsv_dl=tb&rsv_enter=0&rsv_btype=t&bs=%E9%BE%99%E7%AC%A6%20%E4%B8%8B%E8%BD%BD&rsv_sid=undefined&_ss=1&clist=&hsug=&f4s=1&csor=0&_cr1=31293'

search_response = requests.get(
    search_url,
    headers=headers,
).content.decode()

search_tree = etree.HTML(search_response)
response_names = search_tree.xpath('/html/body/div[2]/div[13]/div[3]/div/h3/a')
response_urls = search_tree.xpath(
    '/html/body/div[2]/div[13]/div[3]/div/h3/a/@href')

# print(search_response)
# print(response_names)
for i in response_names:
    i = etree.tostring(i, xml_declaration=True, encoding='utf-8').decode()
    name = re.search(r'>(.*?)</a>', i)[1].replace('<em>',
                                                  '').replace('</em>', '')
    url = re.search(r'href=\"(.*?)\"', i)[1]
    print(name, url)
