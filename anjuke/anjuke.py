# -*- coding: utf-8 -*-
# @Time    : 2021/8/23 16:27
# @Author  : Caokun
# @FileName: anjuke.py
# @Software: PyCharm
from shlex import join
import xlwt
import requests
from bs4 import BeautifulSoup

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('sheet1',cell_overwrite_ok=True)

# 设置表头
worksheet.write(0, 0, label='小区')
worksheet.write(0, 1, label='楼盘')
worksheet.write(0, 2, label='总价')
worksheet.write(0, 3, label='单价')
worksheet.write(0, 4, label='规格')
worksheet.write(0, 5, label='详细')
worksheet.write(0, 6, label='地区')
worksheet.write(0, 7, label='街道')
worksheet.write(0, 8, label='详细地址')
worksheet.write(0, 9, label='卖家')
val1 = 1
val2 = 1
val3 = 1
val4 = 1
val5 = 1
val6 = 1
val7 = 1
val8 = 1
val9 = 1
val10 = 1




def get_html(page_num):
    headers = {
        'cookie': 'sessid=04351FA7-236F-34B0-A3AC-C5BB4E19CA76; aQQ_ajkguid=88C07CFD-D3D3-ADF1-9DFF-240EC2D0B230; twe=2; id58=e87rkGEjW4JzxytdAzucAg==; 58tj_uuid=99b4fe2a-c3cf-4a65-a41a-24eef4801f24; _ga=GA1.2.523729052.1629707137; _gid=GA1.2.1324214258.1629707137; als=0; isp=true; ajk-appVersion=; fzq_h=3fcdda89e1337d2693169e30ca2132d3_1629707211533_ed4fc47b36744c6390fa0e12d41f378b_2043220244; ctid=26; init_refer=; new_uv=4; _gat=1; obtain_by=2; new_session=0; xxzl_cid=2404edf2387f4a8c873171a12cc32929; xzuid=a199dfa5-d2b1-42ef-bfdc-b8cee2fecf22; fzq_js_anjuke_ershoufang_pc=8bee82add799d0a48f05a9fc57df3aed_1629736640765_24',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    html = requests.get(url='https://zhengzhou.anjuke.com/sale/p%s/?from=esf_list'%(page_num), headers=headers)
    return html

def get_data(html_data):
    try:
        html_data.encoding='utf-8'
        soup = BeautifulSoup(html_data.text, 'html.parser')
        return soup
    except Exception as e:
        return e
def clean_data(data):
    for i in data.find(class_="list-left").find_all(class_="list")[0].find_all(class_="property"):
        content = i.find_all(class_="property-content")[0]
        attribute = []
        info_text = []
        address = []
        extra = []
        for i in content.find_all('p')[0].find_all('span'):
            attribute.append(i.string.strip())
        for i in range(1, len(content.find_all(class_="property-content-info-text"))):
            info_text.append(content.find_all(class_="property-content-info-text")[i].string.strip())
        for i in content.find_all(class_="property-content-info-comm-address")[0].find_all('span'):
            address.append(i.string)
        for i in content.find_all(class_="property-extra-text"):
            extra.append(i.string)

        dict = {}
        dict['title'] = content.find_all('h3')[0].string
        dict['name'] = content.find_all(class_="property-content-info-comm-name")[0].string.strip()
        dict['num'] = content.find_all(class_="property-price-total-num")[0].string + '万'
        dict['average'] = content.find_all(class_="property-price-average")[0].string.strip()
        dict['attribute'] = attribute
        dict['info_text'] = info_text
        dict['area'] = address[0]
        dict['street'] = address[1]
        dict['address'] = address[2]
        dict['extra'] = extra
        return dict



def write_excel(data):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1', cell_overwrite_ok=True)

    # 设置表头
    worksheet.write(0, 0, label='小区')
    worksheet.write(0, 1, label='楼盘')
    worksheet.write(0, 2, label='总价')
    worksheet.write(0, 3, label='单价')
    worksheet.write(0, 4, label='规格')
    worksheet.write(0, 5, label='详细')
    worksheet.write(0, 6, label='地区')
    worksheet.write(0, 7, label='街道')
    worksheet.write(0, 8, label='详细地址')
    worksheet.write(0, 9, label='卖家')
    val1 = 1
    val2 = 1
    val3 = 1
    val4 = 1
    val5 = 1
    val6 = 1
    val7 = 1
    val8 = 1
    val9 = 1
    val10 = 1

    for key, value in data.items():
        if key == "title":
            worksheet.write(val1, 0, value)
            val1 += 1
        elif key == "name":
            worksheet.write(val2, 1, value)
            val2 += 1
        elif key == "num":
            worksheet.write(val3, 2, value)
            val3 += 1
        elif key == "average":
            worksheet.write(val4, 3, value)
            val4 += 1
        elif key == "attribute":
            worksheet.write(val5, 4, value)
            val5 += 1
        elif key == "info_text":
            worksheet.write(val6, 5, value)
            val6 += 1
        elif key == "area":
            worksheet.write(val7, 6, value)
            val7 += 1
        elif key == "street":
            worksheet.write(val8, 7, value)
            val8 += 1
        elif key == "address":
            worksheet.write(val9, 8, value)
            val9 += 1
        elif key == "extra":
            worksheet.write(val10, 9, value)
            val10 += 1
    workbook.save('anjuke.xls')

for i in range(49):
    html = requests.get(url='https://zhengzhou.anjuke.com/sale/p{0}/?from=esf_list'.format(i+1),headers=headers)
    # print(html.text)
    # html = open(r'D:\Thief\demo.html', 'r', encoding='utf-8')
    html.encoding='utf-8'
    soup = BeautifulSoup(html.text, 'html.parser')
    try:
        assert '访问验证' in soup.title.string
        print('访问失败')
    except :
        for i in soup.find(class_="list-left").find_all(class_="list")[0].find_all(class_="property"):
            content = i.find_all(class_="property-content")[0]
            attribute = []
            info_text = []
            address = []
            extra = []
            for i in content.find_all('p')[0].find_all('span'):
                attribute.append(i.string.strip())
            for i in range(1, len(content.find_all(class_="property-content-info-text"))):
                info_text.append(content.find_all(class_="property-content-info-text")[i].string.strip())
            for i in content.find_all(class_="property-content-info-comm-address")[0].find_all('span'):
                address.append(i.string)
            for i in content.find_all(class_="property-extra-text"):
                extra.append(i.string)
            dict = {}
            dict['title'] = content.find_all('h3')[0].string
            dict['name'] = content.find_all(class_="property-content-info-comm-name")[0].string.strip()
            dict['num'] = content.find_all(class_="property-price-total-num")[0].string + '万'
            dict['average'] = content.find_all(class_="property-price-average")[0].string.strip()
            dict['attribute'] = attribute
            dict['info_text'] = info_text
            dict['area'] = address[0]
            dict['street'] = address[1]
            dict['address'] = address[2]
            dict['extra'] = extra
            for key, value in dict.items():
                if key == "title":
                    worksheet.write(val1, 0, value)
                    val1 += 1
                elif key == "name":
                    worksheet.write(val2, 1, value)
                    val2 += 1
                elif key == "num":
                    worksheet.write(val3, 2, value)
                    val3 += 1
                elif key == "average":
                    worksheet.write(val4, 3, value)
                    val4 += 1
                elif key == "attribute":
                    worksheet.write(val5, 4, value)
                    val5 += 1
                elif key == "info_text":
                    worksheet.write(val6, 5, value)
                    val6 += 1
                elif key == "area":
                    worksheet.write(val7, 6, value)
                    val7 += 1
                elif key == "street":
                    worksheet.write(val8, 7, value)
                    val8 += 1
                elif key == "address":
                    worksheet.write(val9, 8, value)
                    val9 += 1
                elif key == "extra":
                    worksheet.write(val10, 9, value)
                    val10 += 1

workbook.save('anjuke.xls')