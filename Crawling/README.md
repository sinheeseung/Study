# Crawling

## Lecture1

### Requests Library

정의 : Python에서 HTTP 요청을 보내는 모듈

API
  PUT : PUT 방식으로 요청되며 data 매개변수를 지원
  GET : GET 방식으로 요청되며 params 매개변수를 지원
  POST
  DELETE

응답데이터(Response)
  status_conde : 응답 code를 확인
  headers : headers정보를 확인
  cookies : cookies정보를 확인
  encoding : 데이터 인코딩을 확인할 수 있다.
  text : str 타입의 데이터 일 경우 사용
  content : bytes 타입의 데이터 일 경우 사용
  json() : dict 타입의 데이터 일 경우 사용

## Lecture2

### BeautifulSoup Library

HTML 문서를 탐색해서 원하는 부분만 쉽게 뽑아낼 수 있게 해줌

분류방식(parser)
  html.parser
  lxml : xml 파일 지원
  xml : xml 파일 지원
  html5lib : 브라우저와 같은 방식

주로 사용하는 함수
  select :  해당 태그를 가지는 모든 값 가져오기
  select_one : 해당 태그를 가지는 태그 하나 가져옴
  find : 해당 태그를 가지는 첫번째 태그 가져옴
  find_all : 해당 태그를 가지는 모든 값 가져오기
  Get_text : 태그의 value를 바로 가져올 수 있음

  
  css 선택자()
    태그 선택자 = 태그의 이름으로 선택
      ex) h1, a
    id 선택자 = id값으로 선택
               '#'사용
    class 선택자 = class 이름으로 선택
                  '.'사용
    자식 선택자 = 내가 원하는 태그에 별명이 없을 때 사용
                 바로 아래에 있는 태그를 선택
      ex) .logo_sports > span   => logo_sports라는 class 밑의 span 태그 선택

  ex) soup.select(css선택자)