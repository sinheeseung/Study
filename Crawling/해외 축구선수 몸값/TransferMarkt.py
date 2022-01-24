import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# requsts.get()으로 url정보 요청하기
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}

url = 'https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop'

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

player_info = soup.findAll('tr', class_=['odd', 'even'])

number = []
name = []
position = []
age = []
nation = []
team = []
value = []

for info in player_info:
    player = info.find_all("td")
    number.append(player[0].text)
    name.append(player[3].text)
    position.append(player[4].text)
    age.append(player[5].text)
    nation.append(player[6].img['alt'])  # img 태그의 alt 속성
    team.append(player[7].img['alt'])
    value.append(player[8].text.strip())
print(team)
print(value)