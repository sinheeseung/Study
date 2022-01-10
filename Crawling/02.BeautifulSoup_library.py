import requests
from bs4 import BeautifulSoup
#내가 원하는 HTML 태그 선택 가능

# naver 서버에 정보 요청
response = requests.get("https://www.naver.com")

# naver에서 html 전달
html = response.text

soup = BeautifulSoup(html, 'html.parser')

# 해당 태그를 가지는 부분 찾아냄
word = soup.select_one('#NM_set_home_btn')
#태그의 id값 사용  => id값의 경우 앞에 #

# 텍스트 요소만 출력
print(word.text)

