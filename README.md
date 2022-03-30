# Macro_LightPollutionMap
Light Pollution Map 홈페이지에서 SQM (Sky Quality Meter)를 받아오는 매크로  
같은 경로상의 rootkey.csv 에 저장된 latitude, longitude 를 읽은후 
크롬 홈페이지 매크로 작업을 통해 SQM 값만을 추출한 뒤 
x, y, SQM 형식으로 csv 파일로 저장함 (=sqmResult)

go to Light Pollution Map : https://www.lightpollutionmap.info/

# How To Use
1. 폴더에있는 rootkey.csv 파일에 위도 경도 좌표 추가 및 수정  
2. selenium 을 사용하기 때문에 chromedriver 필수  (rootkey.csv, chromedriver가 실행파일(.exe or .py)과 같은 경로상에 있어야함) 


+ Python 3.9 Version으로 작업
+ Chrome 99ver, 100ver 동작 확인
