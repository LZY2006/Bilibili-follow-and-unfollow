#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import time
import os
import datetime
import pytz
##import sys


# In[2]:
time.sleep(5)

url = "https://api.bilibili.com/x/relation/modify"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Content-Length": "76",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": open("cookie.txt", "r").read(),
    "Host": "api.bilibili.com",
    "Origin": "https://space.bilibili.com",
    "Referer": "https://space.bilibili.com/253119876/fans/follow",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
          }
data = {
    "fid": "322892",
    "act": "1",             # 2代表取关 1代表关注
    "re_src": "11",
    "jsonp": "jsonp",
    "csrf": "7a93837eff26a3251ba9b9d66b74ee96"
       }
fid="322892"


# In[3]:


def unfollow(fid, csrf="7a93837eff26a3251ba9b9d66b74ee96"):
    data = {
    "fid": fid,
    "act": "2",             # 2代表取关 1代表关注
    "re_src": "11",
    "jsonp": "jsonp",
    "csrf": csrf
       }
    r = requests.post(url, headers=headers, data=data)
    return r.text
    
def follow(fid, csrf="7a93837eff26a3251ba9b9d66b74ee96"):
    data = {
    "fid": fid,
    "act": "1",             # 2代表取关 1代表关注
    "re_src": "11",
    "jsonp": "jsonp",
    "csrf": csrf
       }
    r = requests.post(url, headers=headers, data=data)
    return r.text


# In[4]:


do_list = ["322892", "808171", "375375", "391679"]


# In[5]:


HOMEPATH = os.path.expandvars("%HOMEPATH%")
try:
    if not os.path.exists(r"{}/.BiliBiliUnfollowFollow".format(HOMEPATH)):
        os.mkdir(r"{}/.BiliBiliUnfollowFollow".format(HOMEPATH))
except:
    print("创建日志文件失败")
    quit()


# In[6]:


step=0
log_file = open("{}/.BiliBiliUnfollowFollow/debug.log".format(HOMEPATH), "a")


# In[7]:

try:    
    while True:
        step += 1
        for i in do_list:
            result = unfollow(i)
            
            print(result, end=" ")
            log_file.write(str(datetime.datetime.fromtimestamp(time.time(), pytz.timezone("Asia/Shanghai")))+"\n")
            log_file.write(result+" ")
            
            time.sleep(2.5)
            result = follow(i)
            print(result)
            log_file.write(str(datetime.datetime.fromtimestamp(time.time(), pytz.timezone("Asia/Shanghai")))+"\n")
            log_file.write(result+"\n")
            
            time.sleep(2.5)
        time.sleep(5)
        print("step:",step)
        #log_file.write("step:"+str(step)+"\n")
        log_file.close()
        log_file = open("{}/.BiliBiliUnfollowFollow/debug.log".format(HOMEPATH), "a")
except Exception as e:
    log_file.write(str(datetime.datetime.fromtimestamp(time.time(), pytz.timezone("Asia/Shanghai")))+"\n")
    log_file.write(repr(e)+"\n")
    log_file.close()
    quit()
