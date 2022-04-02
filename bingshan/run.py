# -*- coding: utf-8 -*-
# @Time    : 2021/12/7 16:34
# @Author  : Caokun
# @FileName: run.py
# @Software: PyCharm
from bingshan.city_IcebergInfo import city_IcebergInfo
from bingshan.index_info import Index


def run():
    Index().run()
    city_IcebergInfo().run()

if __name__ == '__main__':
    run()