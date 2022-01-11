import requests
from bs4 import BeautifulSoup

query = input()
page = int(input())

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=" + query + "&start=" + str(page*10-9)

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit")

for link in links:
    title = link.text
    url = link.attrs['href']
    print(title, url)