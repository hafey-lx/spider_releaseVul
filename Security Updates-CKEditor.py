# -*- coding:utf-8 -*-

'''
author: 南瓜 pump
date:   2021-10
'''

import requests
import time


def enum_version():
    for x in range(4, 17):
        print(x)                # 显示进度
        for y in range(0, 20):
            url = "https://ckeditor.com/cke4/release/CKEditor-4.{}.{}".format(x, y)
            try:
                resp = requests.get(url, timeout=1)
                if "Security Updates" in resp.text:
                    print("*****************安全修复公告版本：4." + str(x) + '.' + str(y))
                if resp.status_code == 404:
                    print("最大修订版本号：4.", str(x) + "." + str(y-1))
                    break
            except:
                print("访问error：4." + str(x) + '.' + str(y))




# 测试，
# 判断依据：不存在页面会返回404。
# 设置合适的超时时间：设置3访问要25秒，设置1要9秒，设置0.5要5秒。但0.5有时会超时，所以设置为1。推测是网络问题，科学上网应该会更快
# url = "https://ckeditor.com/cke4/release/CKEditor-4.17.0"
# a = time.time()
#
# resp = requests.get(url, timeout=0.5)
#
# print(resp.status_code)
# b = time.time()
# print(b-a)

if __name__ == '__main__':
    enum_version()
