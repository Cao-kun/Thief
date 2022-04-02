# -*- coding: utf-8 -*-
# @Time    : 2021/12/7 14:47
# @Author  : Caokun
# @FileName: iceberg.py
# @Software: PyCharm
import json
import os
import time

import requests
import xlwt

class Iceberg():
    def __init__(self):
        self.workbook = xlwt.Workbook(encoding='utf-8')
        self.filename = r'D:\Thief\file\iceberg\冰山报告-%s.xls'%(time.strftime('%Y-%m-%d'))
        self.headers = {
            'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJvWmdfMnZ5RnJOOVFWMzJpaUN5ZDY2QmRqRF9nIiwiY3JlYXRlZCI6MTY0MjQ3NjE4Nzk0OCwiZXhwIjoxNjQyNTE5Mzg3fQ.Ivww9KHwZNi6EXR82m0q4Q81CHeJwItQ4ePDQUKk0Jp0nXHBac0C18Vd5tIr9kkXOmfr8iC9orm36qk6kG6KrA'
        }
        # 城市id
        self.cityCode = 12
        self.reportPeriod = 242

        with open(r'D:\Thief\bingshan\api.json', 'r', encoding='utf-8') as f:
            self.api = json.loads(f.read())

    def request_api(self,url, headers):
        try:
            response = requests.post(url=url, headers=headers)
            assert response.json()['code'] == 200
            return response.json()
        except Exception as e:
            raise

    def make_dir(self):
        dir_name = r'D:\Thief\file\iceberg\%s'%(time.strftime('%Y_%m_%d'))
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        return dir_name
if __name__ == '__main__':
    path = Iceberg().make_dir()
    print(path)

