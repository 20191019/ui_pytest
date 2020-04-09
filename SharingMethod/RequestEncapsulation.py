# -*- coding:utf-8 -*-
import requests
import json
from SharingMethod import ShengParameter


def get(url, headers):
    print()
    response = requests.get(url=url, headers=headers)
    # 状态码变量，因为后面转成字典无法取值
    rode = response.status_code
    # JSON对象必须是str而不是'Response'，所以使用json.loads()，将r.text转成字典,方便后面断言
    response = json.loads(response.text)
    return response, rode


def post(headers, data, url, url_txt, data_txt, headers_txt):
    # json.dumps 将字典形式的数据转化为字符串
    data = {'data': json.dumps(data)}
    print("开始请求时间：{time}\n"
          "请求参数：\n"
          "  url：{url_txt}\n"
          "  data：{data_txt}\n"
          "  headers：{headers_txt}".format(time=ShengParameter.m_s(), url_txt=url_txt, data_txt=data_txt,
                                           headers_txt=headers_txt))
    response = requests.post(url=url, headers=headers, data=data)
    print("结束请求时间：{time}".format(time=ShengParameter.m_s()))
    rode = response.status_code
    response = json.loads(response.text)
    return response, rode
