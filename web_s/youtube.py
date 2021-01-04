import requests
from bs4 import BeautifulSoup


url = 'https://www.youtube.com/results?search_query=%EC%8B%B9%EC%93%B0%EB%A6%AC'


headers = {
    'authority': 'www.youtube.com',
    'cache-control': 'max-age=0',
    'dpr': '2',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'x-client-data': 'CIa2yQEIo7bJAQjBtskBCKmdygEI06HKAQiGtcoBCJi1ygEI/7zKAQiLv8oBCIfHygEI58jKAQ==',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.youtube.com/',
    'accept-language': 'en-US,en;q=0.9,ko;q=0.8',
    'cookie': 'VISITOR_INFO1_LIVE=2isBw077oMo; CONSENT=YES+KR.ko+201911; LOGIN_INFO=AFmmF2swRQIhAJYp98hnGwJPTatX1BpvTPzktzGUKPB9lklVAYJaHTWvAiB4vOZOMMEGx7fB6x_VICcjps1uSgtjL2wZzIZR31bMDw:QUQ3MjNmd0I2MTRGMFpqSUFCZ1VxdVBhZHQ4SHpqVEtYc1gtSDJXemg4RW9xSHpab0ttck5obVAwREo0RFVQajhBaEtiUDFKdWcySDdXLXBxMDlBbG53a3RiOHcyXzEzTUNNdEw5RDZfUUNXUUw1UWxUdDliS2cweEhwQmhxUml1Yk5JakxZZnZQOS1zenFMS2FpekhIeGo1Q05FQ1pFTWJfRFZDTW1CR09zU0dUdkI1eUpYNmU2RWRZQlBQWTRRN0ZuVFVNRzc3cEtV; PREF=f4=4000000&cvdm=grid&al=en; SID=zweZHUXS4Vdw_aofObSc4-SIZs46mDFjVjH1gOD5r1wIdDzak1ZtOGHZTtlJ7DE0JyhXvQ.; __Secure-3PSID=zweZHUXS4Vdw_aofObSc4-SIZs46mDFjVjH1gOD5r1wIdDzaK7Xvu5auB0FzIEinRzZQPg.; HSID=AgAssRhHetU39NhEi; SSID=A1j1azYj2M0FoQaJn; APISID=T91WS1iXfTjc3vkf/AwGQk82d2X92bLdqZ; SAPISID=-lXCQQWYdbxb4yIM/ANZH0NWZMAYNS5zh2; __Secure-3PAPISID=-lXCQQWYdbxb4yIM/ANZH0NWZMAYNS5zh2; YSC=rF4X0I1jGH4; s_gl=b49ac3bed2c9f40af89303115dbee38ccwIAAABLUg==; SIDCC=AJi4QfGgpfkPqmDoWspq9IBkY5hCrpGQwmayRdZBOoicaBn0FMiUsHbwNiyZ9JrhL7iHGVZyPBA',
}

params = (
    ('search_query', '\uC2F9\uC4F0\uB9AC'),
)

response = requests.get('https://www.youtube.com/results',
                        headers=headers, params=params)

# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://www.youtube.com/results?search_query=%EC%8B%B9%EC%93%B0%EB%A6%AC', headers=headers)


# 목표 :

# 1.광고 영상과 그냥 영상은 나눠져있을 것이다
