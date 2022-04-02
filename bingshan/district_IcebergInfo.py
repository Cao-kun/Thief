# # -*- coding: utf-8 -*-
# # @Time    : 2021/11/2 18:10
# # @Author  : Caokun
# # @FileName: district_IcebergInfo.py
# # @Software: PyCharm
# import time
#
# import requests
# import xlwt
#
# from bingshan.bingshan_base import write_iceberg_infolist, write_activity_infolist
#
#
# class DistrictIcebergInfo():
#     def __init__(self):
#         # 城市 cityCode
#         # 期数  reportPeriod
#         self.workbook = xlwt.Workbook(encoding='utf-8')
#         self.city_iceberginfo_url = 'http://www.bingshandashu.com/icebergapi/cityIcebergInfo'
#         self.district_iceberginfo_url = 'http://www.bingshandashu.com/icebergapi/districtIcebergInfo'
#         self.sub_district_iceberginfo_url = 'http://www.bingshandashu.com/icebergapi/subDistrictIcebergInfo'
#
#         self.headers = {
#             'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJvWmdfMnZ5RnJOOVFWMzJpaUN5ZDY2QmRqRF9nIiwiY3JlYXRlZCI6MTYzODc3Nzg5NDA1MCwiZXhwIjoxNjM4ODIxMDk0fQ.U_pIW8wqHjFCpWsumsYiiZ0SFlK-Ug_35Hah0RRyZSNqj6O0qA2jjJ8y1WVNDhdq34tWZ_voEafbijwn_W-X_Q'
#         }
#         self.reportPeriod = 236
#     def get_citycode(self):
#         params = '?type=1&searchType=1&cityCode=12&reportPeriod=%s'%(self.reportPeriod)
#         city_iceberginfo = requests.post(url=self.city_iceberginfo_url+params, headers=self.headers).json()['data']
#
#         # 获取城市code
#         city_code_info = city_iceberginfo['districtHousePriceRank']
#         city_code_list = []
#         for city_i  in city_code_info:
#             city_code_dict = {}
#             city_code_dict['cityCode']= city_i['cityCode']
#             city_code_dict['cityName']= city_i['cityName']
#             city_code_list.append(city_code_dict)
#
#         # 获取片区code
#         area_code_info = city_iceberginfo['activityInfoList']
#         area_code_list = []
#         for area_i in area_code_info:
#             area_code_dict = {}
#             area_code_dict['cityCode']= area_i['areaCode']
#             area_code_dict['cityName']= area_i['areaName']
#             area_code_list.append(area_code_dict)
#
#         return city_code_list,area_code_list
#
#     def get_district_iceberginfo(self):
#         # 行政区
#         cityCodeList = self.get_citycode()[0]
#
#
#         for cityCode in cityCodeList:
#             params = '?type=1&searchType=1&cityCode=%s&reportPeriod=%s' %(cityCode['cityCode'],self.reportPeriod)
#
#             # 获取城市冰山报告信息
#             district_iceberginfo = requests.post(url=self.district_iceberginfo_url+params, headers=self.headers).json()
#
#
#             # 市场活跃指数
#             icebergInfoList = district_iceberginfo['data']['icebergInfoList']
#             write_iceberg_infolist(icebergInfoList,'%s_市场活跃指数'%(cityCode['cityName']),'郑州数据行政区-%s.xls'%(time.strftime('%Y-%m-%d')))
#
#             #活跃热度排名
#             activityInfoList = district_iceberginfo['data']['activityInfoList']
#             write_activity_infolist(activityInfoList, '%s_活跃热度排名'%(cityCode['cityName']),'郑州数据行政区-%s.xls'%(time.strftime('%Y-%m-%d')))
#
#     def get_sub_district_iceberginfo(self):
#         # 区块
#         cityCodeList = self.get_citycode()[1]
#
#         for cityCode in cityCodeList:
#             params = '?type=1&searchType=1&cityCode=%s&reportPeriod=%s' %(cityCode['cityCode'],self.reportPeriod)
#
#             # 获取区块冰山报告信息
#             sub_district_iceberginfo = requests.post(url=self.sub_district_iceberginfo_url+params, headers=self.headers).json()
#             # 市场活跃指数
#             icebergInfoList = sub_district_iceberginfo['data']['icebergInfoList']
#             write_iceberg_infolist(icebergInfoList,'%s_市场活跃指数'%(cityCode['cityName']),'郑州数据区块-%s.xls'%(time.strftime('%Y-%m-%d')))
#
#             #活跃热度排名
#             activityInfoList = sub_district_iceberginfo['data']['activityInfoList']
#             print(activityInfoList)
#             write_activity_infolist(activityInfoList, '%s_活跃热度排名'%(cityCode['cityName']),'郑州数据区块-%s.xls'%(time.strftime('%Y-%m-%d')))
#     def run(self):
#         self.get_district_iceberginfo()
#         self.get_sub_district_iceberginfo()
#
#
# if __name__ == "__main__":
#     DistrictIcebergInfo().run()
