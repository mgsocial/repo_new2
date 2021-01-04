import requests
from bs4 import BeautifulSoup
​
URL = 'https://1boon.daum.net/ssully/5dd79065bcd34944b2b98307'
​
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
​
news_section = soup.select(
    'alex-area > div > div > div > div.cmt_box > ul.list_comment')
​
for reviews in news_section:
    a_tag = reviews.select_one(
        'li[class=fst] > div[class=cmt_info] > p[class=dexc_txt font_size]')
    print(a_tag)
