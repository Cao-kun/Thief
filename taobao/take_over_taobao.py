# -*- coding: utf-8 -*-
# @Time    : 2022/1/5 10:34
# @Author  : Caokun
# @FileName: take_over_taobao.py
# @Software: PyCharm
import random
from time import sleep

import pyautogui
import win32api

from base.driver import GetDriver


def open_url():
    driver = GetDriver().take_over_driver()

    sleep(3)

    screen_size_wide = win32api.GetSystemMetrics(0)
    screen_size_high = win32api.GetSystemMetrics(1)

    n = random.randint(3, 8)
    # for i in range(n):
    #     x = random.randint(0, screen_size_wide)
    #     y = random.randint(0, screen_size_high)
    #     t = random.randint(1, 5)
    #     print('x坐标为：%s,y坐标为：%s' %(x,y))
    #     pyautogui.moveTo(x, y, duration=0.10 * t)
    li = [{'x': '1170', 'y': '604'}, {'x': '1170', 'y': '604'}, {'x': '1170', 'y': '604'}, {'x': '1170', 'y': '604'}, {'x': '1170', 'y': '604'}, {'x': '1170', 'y': '604'}, {'x': '1170', 'y': '604'}, {'x': '1170', 'y': '604'}, {'x': '1170', 'y': '604'}, {'x': '1170', 'y': '604'}, {'x': '1170', 'y': '604'}]

    for i in li:

        pyautogui.moveTo(int(i['x']),int( i['y']), duration=1)


    driver.find_element_by_xpath("//*[@class='j_expressTbody'][1]/tr[2]/td[2]/ul/li[1]/span/img").click()
    sleep(2)

    pyautogui.moveTo(816, 607, duration=1)

    pyautogui.mouseDown()  # 按下鼠标

    ss = random.randint(30, 60)
    aa = random.randint(15, 23) / 20
    pyautogui.moveTo(816+ss, 607+aa, duration=0.28)

    yy = random.randint(300, 350)
    bb = random.randint(10, 15) / 20
    pyautogui.moveTo(816+yy, 607+bb, duration=(random.randint(20, 31)) / 100)

    pyautogui.mouseUp()  # 松开鼠标
open_url()