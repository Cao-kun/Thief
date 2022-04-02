# -*- coding: utf-8 -*-
# @Time    : 2022/2/8 16:42
# @Author  : Caokun
# @FileName: base_writeExcel.py
# @Software: PyCharm

import xlwt

def edit_data(data):
     new_li = []
     for j in data:
          new_json = {}
          for k, v in j.items():
               if k == 'content':
                    if v['详细信息'] is not None:
                         for _k, _v in v['详细信息'].items():
                              new_json[_k] = _v
                    if v['房源特色'] is not None:
                         for _k, _v in v['房源特色'].items():
                              new_json[_k] = _v
                    if v['户型分间'] is not None:
                         for _k, _v in v['户型分间'].items():
                              new_json[_k] = _v
               else:
                    new_json[k] = v
          new_li.append(new_json)
     return new_li


def get_title(data):
     title = []
     for k, v in data[0].items():
          title.append(k)
     return title


def write_excel(data):
     workbook = xlwt.Workbook(encoding='utf-8')
     # 设置sheet名
     worksheet = workbook.add_sheet('sheetname', cell_overwrite_ok=True)

     new_data = edit_data(data)
     title = get_title(new_data)

     # 设置表头
     for num in range(len(title)):
          worksheet.write(0, num, label=title[num])

     # 写入数据
     row = 1
     for dd in new_data:
          print(dd)
          z = 0
          for i in title:
               v = dd.get(i)

               worksheet.write(row, z, str(v))
               print('行数', row,'列数',z,'数据：',v)
               z += 1
          row += 1

     filename = r'D:\Thief\file\t13.xls'
     workbook.save(filename)