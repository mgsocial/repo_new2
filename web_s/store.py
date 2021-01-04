import requests
from bs4 import BeautifulSoup
import urllib3
import json

search = "마우스"

base_url = f'https://search.shopping.naver.com/search/all?query={search}&cat_id=&frm=NVSHATC'

# res = requests.get(base_url, verify=False)

# soup = BeautifulSoup(res.text, 'html.parser')

# li = soup.select(
#     'div[id=__next] > div > div.container > div.style_inner__18zZX > div.style_content_wrap__1PzEo > div.style_content__2T20F > ul > div > div:nth-child(5) > li > div.basicList_inner__eY_mq > div.basicList_info_area__17Xyo > div.basicList_title__3P9Q7')

# print(li)


# # print(soup)


# 검색했던 결과 가져오기

https: // search.shopping.naver.com/search/all?query = %EB % A7 % 88 % EC % 9A % B0 % EC % 8A % A4 & frm = NVSHATC & prevQuery = %EB % A7 % 88 % EC % 9A % B0 % EC % 8A % A4
