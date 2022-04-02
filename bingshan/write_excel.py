# -*- coding: utf-8 -*-
# @Time    : 2021/12/7 15:39
# @Author  : Caokun
# @FileName: write_excel.py
# @Software: PyCharm
def write_excel(workbook,title,datalist,sheetname,title_us):
    '''
    写入excel操作
    :param workbook: 传入self.workbook类对象
    :param title: 列标题
    :param datalist: 数据
    :param sheetname: sheet名
    :return:
    '''
    # 设置表头
    worksheet = workbook.add_sheet(sheetname, cell_overwrite_ok=True)
    for num in range(len(title)):
        worksheet.write(0, num, label=title[num])

    # 写入数据
    row = 1
    for data in datalist:
        z = 0
        for i in title_us:
            worksheet.write(row, z, data[i])
            # print('行数', row,'列数',z,'数据：',data[i])
            z += 1
        row += 1
