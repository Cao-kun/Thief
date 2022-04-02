# -*- coding: utf-8 -*-
# @Time    : 2021/11/2 16:59
# @Author  : Caokun
# @FileName: city_IcebergInfo.py
# @Software: PyCharm
import datetime
import os
import time

import requests
import xlwt

from bingshan.iceberg import Iceberg
from bingshan.write_excel import write_excel


class city_IcebergInfo(Iceberg):
    '''
    城市层面数据收集
    '''

    def post_cityIcebergInfo(self):
        '''
        请求城市层面数据
        :return: 城市层面数据
        '''
        # 如果没有传入城市id，则遍历所有城市的数据
        urllist = []
        if self.cityCode is not None:
            urllist.append(self.api['cityIcebergInfo'] + '?type=1&searchType=1&cityCode=%s&reportPeriod=%s'%(self.cityCode,self.reportPeriod))
        else:
            pass

        # 传入多城市数据
        self.responselist = []
        for url in urllist:
            response = self.request_api(url=url,headers=self.headers)
            self.responselist.append(response)


    def icebergInfoList(self):
        # 市场活跃指数
        # 循环拿取城市数据
        for response in self.responselist:
            icebergInfoList = response['data']['icebergInfoList']

            # 获取cityname
            cityname = response['data']['cityInfo']['cityName']
            # 设置sheet名字
            sheetname = '%s市场活跃指数' % (cityname)

            # 设置表头
            title = ['城市', '平均价格', '边际价格', '市场活跃指数', '日期']
            title_us = ['cityCode', 'avgPrice', 'marginalPrice', 'activity', 'reportDay']

            # 写入数据
            write_excel(self.workbook, title, icebergInfoList, sheetname, title_us)


    def activityInfoList(self):
        # 市场活跃热度排名TOP30

        # 循环拿取城市数据
        for response in self.responselist:
            activityInfoList = response['data']['activityInfoList']

            # 获取cityname
            cityname = response['data']['cityInfo']['cityName']
            # 设置sheet名字
            sheetname = '%s市场活跃热度排名TOP30'%(cityname)

            # 设置表头
            title = ['排名', '片区名', '平均价格', '边际价格', '市场活跃指数', '更新日期']
            title_us = ['rank', 'areaName', 'avgPrice', 'marginalPrice', 'activity', 'updatedDate']

            # 写入数据
            write_excel(self.workbook, title, activityInfoList, sheetname, title_us)


    def districtHousePriceRank(self):
        # 涨幅排名
        # 循环拿取城市数据
        for response in self.responselist:
            districtHousePriceRank = response['data']['districtHousePriceRank']

            # 获取cityname
            cityname = response['data']['cityInfo']['cityName']
            # 设置sheet名字
            sheetname = '%s市场涨幅排名' % (cityname)

            # 设置表头
            title = ['排名', '片区名', '本月价格', '上月价格', '月环比']
            title_us = ['rank', 'cityName', 'housePrice', 'lastMonthHousePrice', 'mom', 'updatedDate']

            # 写入数据
            write_excel(self.workbook, title, districtHousePriceRank, sheetname, title_us)



    def run(self):
        self.post_cityIcebergInfo()
        self.activityInfoList()
        self.districtHousePriceRank()
        self.icebergInfoList()

    def __del__(self):
        dir_name = self.make_dir()
        filename = r'%s\城市层面数据.xls' % (dir_name)
        self.workbook.save(filename)

if __name__ == "__main__":
    city_IcebergInfo().run()