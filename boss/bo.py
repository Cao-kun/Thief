# -*- coding: utf-8 -*-
# @Time    : 2022/1/6 11:20
# @Author  : Caokun
# @FileName: bo.py
# @Software: PyCharm
from time import sleep

from pyquery import PyQuery as pq
import requests

from base.driver import GetDriver

driver = GetDriver().take_over_driver()
sleep(3)
driver.get('https://www.zhipin.com/c101180100/?query=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&page=1&ka=page-1')
sleep(2)
list = []
for i in range(1,19):
    doc = pq(driver.page_source)
    lis = doc('div.job-list ul li').items()
    for i in lis:
        list.append(i('span.job-area').text())
    driver.find_element_by_xpath('//*[@class="next"]').click()
    sleep(2)

print(list)