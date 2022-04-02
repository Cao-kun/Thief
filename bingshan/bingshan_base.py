# -*- coding: utf-8 -*-
# @Time    : 2021/11/2 18:14
# @Author  : Caokun
# @FileName: bingshan_base.py
# @Software: PyCharm
import xlwt

workbook = xlwt.Workbook(encoding='utf-8')


def write_iceberg_infolist(icebergInfoList, sheetname,filename):
    # 市场活跃指数
    # 调用get_city_iceberginfo（），获取城市冰山报告信息

    lists = ['城市', '平均价格', '边际价格', '市场活跃指数', '日期']
    worksheet = workbook.add_sheet(sheetname, cell_overwrite_ok=True)

    # 设置表头
    for num in range(len(lists)):
        worksheet.write(0, num, label=lists[num])
    row = 1
    for icebergInfo in icebergInfoList:
        # 写入数据
        worksheet.write(row, 0, icebergInfo['cityCode'])
        worksheet.write(row, 1, icebergInfo['avgPrice'])
        worksheet.write(row, 2, icebergInfo['marginalPrice'])
        worksheet.write(row, 3, icebergInfo['activity'])
        worksheet.write(row, 4, icebergInfo['reportDay'])
        row += 1
    workbook.save(filename)


def write_activity_infolist(activityInfoList,sheetname,filename):
    # 市场活跃热度排名TOP30
    # 调用get_city_iceberginfo（），获取城市冰山报告信息

    lists = ['排名', '片区名', '平均价格', '边际价格', '市场活跃指数', '更新日期']
    worksheet = workbook.add_sheet(sheetname, cell_overwrite_ok=True)

    # 设置表头
    for num in range(len(lists)):
        worksheet.write(0, num, label=lists[num])
    row = 1
    for activityInfo in activityInfoList:
        # 写入数据
        worksheet.write(row, 0, activityInfo['rank'])
        worksheet.write(row, 1, activityInfo['areaName'])

        worksheet.write(row, 2, activityInfo['avgPrice'])
        worksheet.write(row, 3, activityInfo['marginalPrice'])

        worksheet.write(row, 4, activityInfo['activity'])
        worksheet.write(row, 5, activityInfo['updatedDate'])
        row += 1
    workbook.save(filename)
