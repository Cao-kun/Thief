# -*- coding: utf-8 -*-
# @Time    : 2022/2/8 16:14
# @Author  : Caokun
# @FileName: base_ershoufang.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup


headers = {
        "Cookie": "lianjia_uuid=e90c3b84-ffdc-4d66-ab34-22217fe961a2; lianjia_ssid=5be190aa-6cce-4830-b476-2f3f4e58ef53; _smt_uid=6201c216.51f7d43e; UM_distinctid=17ed6de278db50-03062852ef89fa-f791539-1fa400-17ed6de278e103f; _jzqc=1; _jzqa=1.4265894658239430000.1644282391.1644282391.1644282391.1; _jzqy=1.1644282391.1644282391.1.jzqsr=baidu.-; _jzqckmp=1; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217ed6de31c0562-046afda7b92b6c-f791539-2073600-17ed6de31c13e5%22%2C%22%24device_id%22%3A%2217ed6de31c0562-046afda7b92b6c-f791539-2073600-17ed6de31c13e5%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1644282394; _ga=GA1.2.1519299404.1644282399; _gid=GA1.2.1749388520.1644282399; select_city=410100; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1644282739; _jzqb=1.16.10.1644282391.1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1",
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }



def xiangxi(path):
    # 详细信息
    dd = {}

    # 基本属性
    base_1 = path.find_all(class_="base")[0]
    li_1 = base_1.find_all("li")
    for i in li_1:
        str = i.text
        k = str[:4]
        v = str[4:]
        dd[k]=v
    try:
        # 交易属性
        base_2 = path.find(class_="transaction").find_all(class_="content")[0]
        li_2 = base_2.find_all("li")
        for j in li_2:
            str = j.text.strip().replace("\n", "")
            z = str[:4]
            x = str[4:]
            dd[z]=x
    except:
        pass

    return dd

def fangyuantese(path):
    # print(path)
    try:
        # 标签
        tags = path.find_all(class_="tags clear")[0]
        li = tags.find_all("a")
        tags_li = []
        for i in li:
            tags_li.append(i.get_text().strip())
        dd = {}
        try:
            # 核心卖点
            baseattribute_li = []
            baseattribute_1 = path.find_all(class_="baseattribute clear")[0].find(class_="content").text.strip()
            baseattribute_2 = path.find_all(class_="baseattribute clear")[1].find(class_="content").text.strip()
            baseattribute_3 = path.find_all(class_="baseattribute clear")[2].find(class_="content").text.strip()
            baseattribute_4 = path.find_all(class_="baseattribute clear")[3].find(class_="content").text.strip()
            baseattribute_li.append(baseattribute_1)
            baseattribute_li.append(baseattribute_2)
            baseattribute_li.append(baseattribute_3)
            baseattribute_li.append(baseattribute_4)
            dd['核心卖点'] = baseattribute_li
        except:
            pass
        dd['标签'] = tags_li
        return dd
    except:
        return None

def huxing(path):
    try:
        # 户型图
        img = path.find("img")['src']
        infoList = path.find_all(id="infoList")[0]
        # 户型
        li_1 = []
        for info in infoList:
            li_2 = []
            for i in info:
                if len(str(i)) > 1:
                    li_2.append(i.text)
            if len(li_2) != 0:
                li_1.append(li_2)
        dd = {}
        dd['户型图'] = img
        dd['户型'] = li_1
        return dd
    except:
        return None



def get_info(url,headers):
    html = requests.get(url=url, headers=headers)
    soup_2 = BeautifulSoup(html.text, 'html.parser')
    box_l = soup_2.find(class_="m-content").find(class_="box-l")
    # <!-- 基本信息 -->
    xiangxi_data = xiangxi(box_l.find(class_="newwrap baseinform"))

    # <!-- 房源特色 -->
    fangyuantese_data  = fangyuantese(box_l.find_all(class_="newwrap baseinform")[1])

    # <!-- 户型分间 -->
    if box_l.find_all(class_="newwrap")[4].find(class_="content") is not None:
        huxing_data  = huxing(box_l.find_all(class_="newwrap")[4].find(class_="content"))
    elif box_l.find_all(class_="newwrap")[3].find(class_="content") is not None:
        huxing_data  = huxing(box_l.find_all(class_="newwrap")[3].find(class_="content"))
    else:
        huxing_data = None
    info = {}
    info['详细信息'] = xiangxi_data
    info['房源特色'] = fangyuantese_data
    info['户型分间'] = huxing_data
    return info

get_info(url='https://zz.lianjia.com/ershoufang/104106388890.html',headers=headers)

def get_one_page_info(data):
    li_all = []
    for i in data.find(class_="sellListContent"):
        info = i.find_all(class_="info clear")[0]

        __flood = info.find_all(class_="flood")[0].find_all(class_="positionInfo")[0]
        xiaoqu = __flood('a')[0].get_text()
        xiaoqudizhi = __flood('a')[0]['href']
        quyu = __flood('a')[1].get_text()

        __title = info.find_all(class_="title")[0]('a')[0]
        href = __title['href']
        title = __title.get_text()


        __priceInfo = info.find_all(class_="priceInfo")[0]
        zongjia = __priceInfo.find_all(class_="totalPrice totalPrice2")[0].find("span").get_text()
        danjia = __priceInfo.find_all(class_="unitPrice")[0].find("span").get_text()

        guanzhu = info.find_all(class_="followInfo")[0].get_text()
        content = get_info(url=href, headers=headers)

        dd_all = {}
        dd_all['房屋名称'] = title
        dd_all['content'] = content
        dd_all['小区信息'] = xiaoqu
        dd_all['小区地址'] = xiaoqudizhi
        dd_all['区域信息'] = quyu
        dd_all['最近关注'] = guanzhu
        dd_all['总价'] = zongjia
        dd_all['单价'] = danjia
        li_all.append(dd_all)
    return li_all

def get_all_page_info():
    all_li = []
    for i in range(19,22):
        shangjie = "https://zz.lianjia.com/ershoufang/shangjiequ/pg%s/"%(i)
        html = requests.get(url=shangjie, headers=headers)
        html.encoding = 'utf-8'
        data = BeautifulSoup(html.text, 'html.parser')
        one_li = get_one_page_info(data)
        all_li.extend(one_li)
        print(all_li)
    return all_li

