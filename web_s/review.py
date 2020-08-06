import requests
from bs4 import BeautifulSoup, NavigableString, Tag

base_url = f'https://movie.naver.com/movie/running/current.nhn'

res = requests.get(base_url)

soup = BeautifulSoup(res.text, 'html.parser')


movies_section = soup.select(
    'div[id=wrap] > div[id=container] > div[id=content] > div.article > div.obj_section > div.lst_wrap > ul > li')

code_list = []
title_list = []
content = []

final_movie_data = []

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

    final_movie_data.append(movie_data)


for movie in final_movie_data:

    code = movie['code']

    headers = {
        'authority': 'movie.naver.com',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'iframe',
        'referer': f'https://movie.naver.com/movie/bi/mi/point.nhn?code={code}#tab',
        'accept-language': 'en-US,en;q=0.9,ko;q=0.8',
        'cookie': 'NNB=QMKZGNI7S36F4; ASID=731711cd000001730d003e0b0000004a; MM_NEW=1; NFS=2; MM_NOW_COACH=1; nx_ssl=2; nid_inf=-1576229663; NID_AUT=FjVIj1I9P8npAf/uAvNoxxwZlauZxWDqCgmFhSdgCDYSYhAeIh7IdO2rd53ngFeV; NID_JKL=17+lUQbWJ2jHmwPwsePuaDKIBrIsj0udp5Wy+hAid5c=; NRTK=ag#30s_gr#3_ma#-2_si#0_en#-2_sp#-2; NM_THUMB_PROMOTION_BLOCK=Y; NV_WETR_LOCATION_RGN_M="MDkxNDAxMDQ="; NV_WETR_LAST_ACCESS_RGN_M="MDkxNDAxMDQ="; BMR=s=1596648173120&r=https%3A%2F%2Fm.post.naver.com%2Fviewer%2FpostView.nhn%3FvolumeNo%3D28625156%26memberNo%3D618343%26vType%3DVERTICAL&r2=https%3A%2F%2Fsearch.naver.com%2Fsearch.naver%3Fsm%3Dtop_hty%26fbm%3D0%26ie%3Dutf8%26query%3D%25EC%259D%25B8%25ED%2594%258C%25EB%25A3%25A8%25EC%2596%25B8%25EC%2584%259C; NID_SES=AAABjQY3ALsCSE+2pAu2ZPF2CVeEfuI1BsMm+EV7Za1RIucdnAE/DnHcvcV8ShJ0qHxv57eBeWZoRUdQyAlFFm7cj7H25z1BXjK1zbA0c8upAmi8c7S+w5Ez/j0VjpkqGACoJLYRZ+iAzTBo2O3YWYaBWeieyvGUxSqPoE9nV3G/d/J5sxB9cuDbznOdPhZrlo3FiFcRaOT+jo5pBxO/0QVY5rn3oTzC0BIl+JAuLvI4vP4TPbUo/uL8wA0SEosF9IN02oDq9UKulsKQXd4Ob2dnPiJlFMGDUHuil7wP54FTC5xx2pM5lyFe704mfwsZqtme0ovcovQ6osMQUoSWQXwkoauVbDpziVzHHW5WYcvCxmtueELj/5F93C4do872wvrufuFTuugv2ARQhZa386X8a495Uq0TkbjS3cXtPKtpCsxnjluOr8vJQ0jyyOjeaQRiCNnCVOMNrvUvo6imlgaYg9JnIVdEYKIWiHREdIiUZW9f4vhuQ42Sh2dFL/8NkG8xAv1D41KVSajOLC3WnBKn40I=; page_uid=UyXrtlprvmsssbWB8LKsssssstl-484104; csrf_token=7f771fc6-b46d-4295-a0ea-5daddb66b53c',
    }
    params = (
        ('code', f'{code}'),
        ('type', 'after'),
        ('isActualPointWriteExecute', 'false'),
        ('isMileageSubscriptionAlready', 'false'),
        ('isMileageSubscriptionReject', 'false'),
    )

    response = requests.get(
        'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', headers=headers, params=params)

    soup = BeautifulSoup(response.text, 'html.parser')

    review_list = soup.select('body > div > div > div.score_result > ul')

    count = 0

    for review in review_list:
        score = review.select_one('div.star_score > em').text

        if review.select_one(f'iv.score_reple > p > span#_filtered_ment_{count} > span#_unfold_ment{count}'):
            reple = review.select_one(
                f'div.score_reple > p > span#_filtered_ment_{count} > p > span#_unfold_ment9').text.strip()

        else:
            reple = review.select_one(
                f'div.score_reple > p > span#_filtered_ment_{count}').text.strip()

            count += 1

        print(score, reple.strip())


#     content.append(movie_data)
#     code_list.append(movie_code)

# for m in code_list:
#     code = m

    # headers = {
    #     'authority': 'movie.naver.com',
    #     'upgrade-insecure-requests': '1',
    #     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #     'sec-fetch-site': 'same-origin',
    #     'sec-fetch-mode': 'navigate',
    #     'sec-fetch-dest': 'iframe',
    #     'referer': f'https://movie.naver.com/movie/bi/mi/point.nhn?code={code}#tab',
    #     'accept-language': 'en-US,en;q=0.9,ko;q=0.8',
    #     'cookie': 'NNB=QMKZGNI7S36F4; ASID=731711cd000001730d003e0b0000004a; MM_NEW=1; NFS=2; MM_NOW_COACH=1; nx_ssl=2; nid_inf=-1576229663; NID_AUT=FjVIj1I9P8npAf/uAvNoxxwZlauZxWDqCgmFhSdgCDYSYhAeIh7IdO2rd53ngFeV; NID_JKL=17+lUQbWJ2jHmwPwsePuaDKIBrIsj0udp5Wy+hAid5c=; NRTK=ag#30s_gr#3_ma#-2_si#0_en#-2_sp#-2; NM_THUMB_PROMOTION_BLOCK=Y; NV_WETR_LOCATION_RGN_M="MDkxNDAxMDQ="; NV_WETR_LAST_ACCESS_RGN_M="MDkxNDAxMDQ="; BMR=s=1596648173120&r=https%3A%2F%2Fm.post.naver.com%2Fviewer%2FpostView.nhn%3FvolumeNo%3D28625156%26memberNo%3D618343%26vType%3DVERTICAL&r2=https%3A%2F%2Fsearch.naver.com%2Fsearch.naver%3Fsm%3Dtop_hty%26fbm%3D0%26ie%3Dutf8%26query%3D%25EC%259D%25B8%25ED%2594%258C%25EB%25A3%25A8%25EC%2596%25B8%25EC%2584%259C; NID_SES=AAABjQY3ALsCSE+2pAu2ZPF2CVeEfuI1BsMm+EV7Za1RIucdnAE/DnHcvcV8ShJ0qHxv57eBeWZoRUdQyAlFFm7cj7H25z1BXjK1zbA0c8upAmi8c7S+w5Ez/j0VjpkqGACoJLYRZ+iAzTBo2O3YWYaBWeieyvGUxSqPoE9nV3G/d/J5sxB9cuDbznOdPhZrlo3FiFcRaOT+jo5pBxO/0QVY5rn3oTzC0BIl+JAuLvI4vP4TPbUo/uL8wA0SEosF9IN02oDq9UKulsKQXd4Ob2dnPiJlFMGDUHuil7wP54FTC5xx2pM5lyFe704mfwsZqtme0ovcovQ6osMQUoSWQXwkoauVbDpziVzHHW5WYcvCxmtueELj/5F93C4do872wvrufuFTuugv2ARQhZa386X8a495Uq0TkbjS3cXtPKtpCsxnjluOr8vJQ0jyyOjeaQRiCNnCVOMNrvUvo6imlgaYg9JnIVdEYKIWiHREdIiUZW9f4vhuQ42Sh2dFL/8NkG8xAv1D41KVSajOLC3WnBKn40I=; page_uid=UyXrtlprvmsssbWB8LKsssssstl-484104; csrf_token=7f771fc6-b46d-4295-a0ea-5daddb66b53c',
    # }

    # params = (
    #     ('code', f'{code}'),
    #     ('type', 'after'),
    #     ('isActualPointWriteExecute', 'false'),
    #     ('isMileageSubscriptionAlready', 'false'),
    #     ('isMileageSubscriptionReject', 'false'),
    # )

    # response = requests.get(
    #     'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', headers=headers, params=params)

#     soup = BeautifulSoup(response.text, 'html.parser')

#     select = soup.select(
#         'body > div > div > div.score_result > ul > li > div.star_score')

#     score_list = []
#     content_list = []

#     for review in select:
#         review_dict = {}
#         score_list.append(review.select_one('em'))

#         for i in range(10):
#             content_list.append(review.select_one(
#                 f'p> #_filtered_ment_{i}').text)

#         print(score_list, content_list)
