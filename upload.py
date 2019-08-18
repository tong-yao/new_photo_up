# -*- coding: utf-8 -*-

import upyun,os
import hashlib

# 需要填写自己的服务名，操作员名，密码
service = "qukanba-test"
username = "zhaoyining"
password = "QrNy0WvD9BTfPW3lWIes14vOg4Sg7N12"

# 需要填写上传文件的本地路径和云存储路径，视频
local_file = ""
remote_file = ""
# local_file = "9a187c024f998516ab7fac15a53b90c8.mp4"
# remote_file = "testsss_video/0c8.mp4"

path = "/home/photo2/"
files = os.listdir(path)
#
# for i in files:
# # 填写要上传的图片
#     img_file = i.strip("photo")  #mysql 表里的
#     re_file = "img/Bran Stark2000.jpg"

up = upyun.UpYun(service, username=username, password=password)


def rest_upload():
    for i in files:
        # 填写要上传的图片
        i = i.strip("photo")
        img_file = i  # mysql 表里的
        re_file = "img/{}".format(i)

        with open(img_file, "rb") as f:
            # headers 可选，见rest上传参数
            headers = None
            up.put(re_file, f, headers=headers)

rest_upload()


