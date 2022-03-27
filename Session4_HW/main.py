import requests
from bs4 import BeautifulSoup
from webtoon import extract_info
import csv

file = open('webtoonmon.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["title", "author", "rating"])

final_result = []

WEBTOON_URL = f'https://comic.naver.com/webtoon/weekdayList?week=mon'
webtoon_html = requests.get(WEBTOON_URL)
webtoon_mon = BeautifulSoup(webtoon_html.text, "html.parser")

webtoon_list_box = webtoon_mon.find("ul", {"class":"img_list"})
webtoon_list = webtoon_list_box.find_all("li")

final_result += extract_info(webtoon_list)

for result in final_result:
    row = []
    row.append(result['title'])
    row.append(result['author'])
    row.append(result['rating'])
    writer.writerow(row)
print(final_result)