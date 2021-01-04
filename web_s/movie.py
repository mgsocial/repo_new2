import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import re

base_url = 'https://movie.naver.com/movie/running/current.nhn'

res = requests.get(base_url)

soup = BeautifulSoup(res.text, 'html.parser')


movies_section = soup.select(
    'div[id=wrap] > div[id=container] > div[id=content] > div.article > div.obj_section > div.lst_wrap > ul > li')

code_list = []

title_list = []


# for movie in movies_section:
#     if isinstance(movie, NavigableString):
#         continue
#     if isinstance(movie, Tag):
#         a_tag = movie.select_one('dl > dt > a')
#         title = a_tag.text
#         title_list.append(title)

#         code = a_tag['href'][-6:].replace("=", "")
#         code_list.append(code)

#     print(title)
#     print(code)

content = []

for movie in movies_section:
    movie_dict = {}
    a_tag = movie.select_one('dl > dt > a')

    movie_link = a_tag['href']
    movie_title = a_tag.getText()
    movie_code = movie_link.split('=')[1]

    movie_data = {
        'title': movie_title,
        'code': movie_code
    }

    content.append(movie_data)

print(content)
