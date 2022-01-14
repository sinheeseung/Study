import requests
from bs4 import BeautifulSoup

# 종목 코드 리스트
codes = [
    '005930',
    '000660',
    '035720'
]

companys = [
    '삼성전자',
    'SK하이닉스',
    '카카오'
]
for i in range(len(codes)):
    url = f"https://finance.naver.com/item/sise.naver?code={codes[i]}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    price = soup.select_one("#_nowVal").text
    price = price.replace(',','')
    print(f"{companys[i]}의 현재 주가는 {price}입니다.")