# -*- coding = utf-8 -*-
# @Time : 2020/4/1922:41
# @Author : SXW
# @File : spider.py
# @Software : PyCharm


from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
import sqlite3


def main():
    beseurl = "https://movie.douban.com/top250?start="
    #1.爬取网页
    datalist = getData(beseurl)
    savepath = ".\\豆瓣电影Top250.xls"
    #3.保存数据
    # saveData(savepath)

    askURL("https://movie.douban.com/top250?start=0")


#爬取网页
def getData(beseurl):
    datalist = []
    #2.逐一解析数据
    return datalist


#得到指定一个URL的网页内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
                      "537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }
                 #用户代理：表示告诉豆瓣服务器，我们是什么类型的机器

    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)


#保存数据
def saveData(savepath):
    print("save....")


if __name__ == "__main__":
    main()
