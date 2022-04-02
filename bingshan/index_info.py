# -*- coding: utf-8 -*-
# @Time    : 2021/12/7 15:00
# @Author  : Caokun
# @FileName: index_info.py
# @Software: PyCharm
import json
import time

from bingshan.iceberg import Iceberg
from bingshan.write_excel import write_excel


class Index(Iceberg):
    '''
    首页信息数据
    '''
    def post_index(self):
        '''
        请求首页数据
        :return: 首页数据
        '''
        self.response = self.request_api(url=self.api['index'],headers=self.headers)

    def coreHousePriceRankList(self):
        '''
        获取核心城市排行
        :return:
        '''
        # 获取核心城市排行
        datalist = self.response['data']['coreHousePriceRankList']
        # 设置sheet名字
        sheetname = '核心城市排行'

        # 设置表头
        title = ['级别', '排名', '城市', '本月房价', '上月房价', '月环比' ]
        title_us = ['cityType','rank','cityName','housePrice','lastMonthHousePrice','mom']

        # 写入数据
        write_excel(self.workbook, title, datalist, sheetname,title_us)
    def housePriceRankList(self):
        '''
        获取城市排行
        :return:
        '''
        # 获取城市排行
        datalist = self.response['data']['housePriceRankList']
        # 设置sheet名字
        sheetname = '城市排行'

        # 设置表头
        title = ['级别', '排名', '城市', '本月房价', '上月房价', '月环比' ]
        title_us = ['cityType','rank','cityName','housePrice','lastMonthHousePrice','mom']

        # 写入数据
        write_excel(self.workbook, title, datalist, sheetname,title_us)

    def run(self):
        self.post_index()
        self.coreHousePriceRankList()
        self.housePriceRankList()

    def __del__(self):
        dir_name = self.make_dir()
        filename =  r'%s\首页信息数据.xls'%(dir_name)
        self.workbook.save(filename)

if __name__ == "__main__":
    Index().run()