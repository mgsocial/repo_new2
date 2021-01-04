
import pandas as pd
import requests
from bs4 import BeautifulSoup
URL = "https://comment.daum.net/apis/v1/posts/137626313/comments?parentId=0&offset=0&limit=3&sort=LATEST&isInitial=true&hasNext=true"
response = requests.get(URL)
# print(response.text)
df = pd.DataFrame(response.json())
# print(df)
df = df['content']
print(df)
