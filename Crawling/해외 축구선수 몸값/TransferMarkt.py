import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# 최대 열 수 설정
pd.set_option('display.max_columns',500)

# 표시 할 가로의 길이
pd.set_option('display.width', 1000)
# requsts.get()으로 url정보 요청하기
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}

number = []
name = []
position = []
age = []
nation = []
team = []
value = []

for i in range(1,3):
    url = f'https://www.transfermarkt.com/marktwertetop/wertvollstespieler?page={i}'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    player_info = soup.findAll('tr', class_=['odd', 'even'])

    for info in player_info:
        player = info.find_all("td")
        number.append(int(player[0].text))
        name.append(player[3].text)
        position.append(player[4].text)
        age.append(player[5].text)
        nation.append(player[6].img['alt'])  # img 태그의 alt 속성
        team.append(player[7].img['alt'])
        value.append(player[8].text.strip()) # 공백제거

df = pd.DataFrame(
    {"number": number,
     "name": name,
     "position": position,
     "age": age,
     "nation": nation,
     "team": team,
     "value": value}
)

df.to_csv('TransferMarkt50.csv', index=False)

# 정렬
print(df.sort_index(ascending=False).head())
print()
print(df.sort_values("age", ascending=False).head())
print()

# 컴럼 이름 바꾸기
df.rename(columns={'team':'club'}, inplace=True)

# 데이터 전처리 => value에서 불필요한 문자 제거, float타입
df['value'] = df['value'].str.replace('€', '')
df['value'] = df['value'].str.replace('m', '').astype('float')

# 컬럼 생성
df['시장가치(억)'] = df['value']*13

# 컬럼 삭제
df.drop(columns=['value'], inplace=True)
print(df)