import os
import random
import time
from concurrent.futures import ThreadPoolExecutor
from urllib import parse, request

import requests

from my_utils import RandUA

UA = RandUA()
IMG_FOLDER = "./resources/honor_of_kings/"


def download_img(img_url: str, img_path: str, img_name: str):
    img_fp = f'{img_path}/{img_name}.jpg'
    try:
        request.urlretrieve(img_url, img_fp)
        print(f"图片 {img_name} 下载成功")
    except Exception:
        print(f"!!!!!!图片 {img_name} 下载失败!!!!!!")


def handle_json_info(page):
    url = 'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi'
    time_stamp = int(time.time() * 1000)
    pay_load = {
        "activityId": "2735",
        "sVerifyCode": "ABCD",
        "sDataType": "JSON",
        "iListNum": "20",
        "totalpage": "0",
        "page": page + 1,
        "iOrder": "0",
        "iSortNumClose": "1",
        "iAMSActivityId": "51991",
        "_everyRead": "true",
        "iTypeId": "2",
        "iFlowId": "267733",
        "iActId": "2735",
        "iModuleId": "2735",
        "_": str(time_stamp)
    }
    try:
        json_data = requests.get(url=url, params=pay_load, headers=UA.simple()).json()['List']
        for img_info in json_data:
            img_name = parse.unquote(img_info['sProdName']).strip()
            img_path = IMG_FOLDER + img_name
            if not os.path.exists(img_path):
                os.mkdir(img_path)
            for i in range(1, 9):
                img_url = parse.unquote(img_info[f'sProdImgNo_{i}']).replace('/200', '/0')
                download_img(img_url, img_path, f'{img_name}_{i}')
    except Exception:
        print(f"!!!!!!第 {page + 1} 页数据获取失败")
    finally:
        time.sleep(random.random())


def main():
    total_page = list(range(32))
    # 12个线程
    with ThreadPoolExecutor(max_workers=12) as pool:
        pool.map(handle_json_info, total_page)


if __name__ == '__main__':
    main()
