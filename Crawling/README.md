# Crawling

## Lecture1

### Requests Library

정의 : Python에서 HTTP 요청을 보내는 모듈

API  
  -PUT : PUT 방식으로 요청되며 data 매개변수를 지원  
  -GET : GET 방식으로 요청되며 params 매개변수를 지원  
  -POST  
  -DELETE  

응답데이터(Response)  
  -status_conde : 응답 code를 확인  
  -headers : headers정보를 확인  
  -cookies : cookies정보를 확인  
  -encoding : 데이터 인코딩을 확인할 수 있다.  
  -text : str 타입의 데이터 일 경우 사용  
  -content : bytes 타입의 데이터 일 경우 사용  
  -json() : dict 타입의 데이터 일 경우 사용  
 
## Lecture2

### BeautifulSoup Library

HTML 문서를 탐색해서 원하는 부분만 쉽게 뽑아낼 수 있게 해줌  

분류방식(parser)  
  -html.parser  
  -lxml : xml 파일 지원  
  -xml : xml 파일 지원  
  -html5lib : 브라우저와 같은 방식  

주로 사용하는 함수  
  -select :  해당 태그를 가지는 모든 값 가져오기  
  -select_one : 해당 태그를 가지는 태그 하나 가져옴  
  -find : 해당 태그를 가지는 첫번째 태그 가져옴  
  -find_all : 해당 태그를 가지는 모든 값 가져오기  
  -Get_text : 태그의 value를 바로 가져올 수 있음  

  
  css 선택자  
    -태그 선택자 = 태그의 이름으로 선택  
      ex) h1, a  
    -id 선택자 = id값으로 선택  
               '#'사용  
    -class 선택자 = class 이름으로 선택  
                  '.'사용  
    -자식 선택자 = 내가 원하는 태그에 별명이 없을 때 사용  
                 바로 아래에 있는 태그를 선택  
      ex) .logo_sports > span   => logo_sports라는 class 밑의 span 태그 선택  
   ex) soup.select(css선택자)  


## Lecture3

### URL

인터넷 주소 형식

Protocol - Domain - Path - Parameter

  -Protocol : http, https  
  -Domain : IP주소에 이름을 부여한 것  
  -Path : 서버에서 해당 페이지의 경로  
  -Parameter : Key과 value로 구성, &로 연결

### Pyautogui

마우스, 키보드 매크로 라이브러리
간단한 입력 창 띄우기에 사용


## Lecture4

### requests의 한계
  
  -로그인이 필요한 사이트  
  -동적으로 HTML을 만드는 경우
    1. 스크롤 하거나 클릭하면 데이터 생성(URL 주소가 변경되지 않았는데 데이터가 변함)  
    2. 표, 테이블 형태의 데이터  

### 셀레니움
  
  브라우저를 실제로 띄워서 사람처럼 동작하도록 만들 수 있다.
  
## Lecture 5

### Pandas

df.shape : 행과 열의 개수 파악  
df.info : 전체 정보 요약  
df.head : 처음 5개 행 보여주기  
df.tail : 마지막 5개 행 보여주기  
df[:10], df.iloc[:10] : 처음 10개 행까지 보여주기  
df.name : 컬럼 이름 선택하기  
df[['name','value']] : 여러개 컬럼 이름 선택하기  
df.loc[:,['name','value]] : ,를 기준으로 행과 열의 이름으로 선택하기  
df.loc[df['age] > 30], ['name','age'] : 조건을 통해 선택하기  

df.sort_index() : 인덱스 기준으로 정렬  
df.sort_values('age') : 컬럼 이름을 기준으로 정렬  
df.set_index('number', inplace=True) : 인덱스를 컬럼 이름으로 설정
df.rename(columns = {'team':'club'}, inplace=True) : 컬럼 이름 변경하고 저장

df['age'].mean() : 특정 컬럼의 평균  
df['시장가치(억)'].sum() : 특정 컬럼의 합  
df['nation'].mode() : 특정 컬림의 최빈값  
df.describe() : 모든 수치형 데이터의 통계  
df.groupby("nation") : 컴럼 이름으로 그룹화  
df.groupby("nation").max() : 그룹화 이후 통계 확인  