# -*- coding: utf-8 -*-
"""
@Date    : 2023/03/01 00:01:57
@Author  : Sonder-MX
@File    : rand_ua.py
@Version : 0.0.1
"""
import random
from typing import Dict, List

import requests


def get_ua() -> List:
    url = 'https://www.useragents.me/api'
    try:
        ua_list = requests.get(url).json()['data']
        data_obj = [ua['ua'] for ua in ua_list]
        return data_obj
    except Exception as e:
        print(f"获取 User Agent 失败！！！{e}")
        return []


class RandProxy:
    """付费的太贵，免费的不能用。。。。。"""

    def __init__(self) -> None:
        pass


class RandUA:
    """
    >>> from rand_proxy import RandUA
    >>>
    >>> ua = RandUA()
    >>>
    >>> handers = { 'User-Agent': ua.rand_ua() }
    or
    >>> requests.get(url=url, headers=ua.simple())
    """

    def __init__(self) -> None:
        self.ua_list = get_ua()

    def rand_ua(self) -> str:
        return random.choice(self.ua_list)

    def simple(self, **kwargs) -> Dict:
        """
        :params kwargs
            Cookie='...'
            Referer='...'
            ...
        """
        headers = {
            'User-Agent': self.rand_ua(),
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language':
            'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Connection': 'keep-alive',
            **kwargs
        }
        return headers
