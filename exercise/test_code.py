import module1 as md #음성 말하고 듣기, 날씨, 미세먼지 가져오는 모듈
import search_code1 as cd1 #검색 모듈
w_25 = md.weather_pm25(37.56, 126.76, '서울') #module1 클래스 객체 선언, 서울 지역 위도 경도로 하드 코딩

md.speak('음성을 입력하세요, <시리야>') #코드 작동 확인, 입력해야할 단어 명시
try:
    audio1 = md.listen()
    if audio1 == '시리야':

        while True:
            md.speak('원하는 정보를 말씀해주세요. 1. 서울 날씨, 2. 서울 미세먼지, 3. 검색, 4. 음악 검색(가수) 5. 종료')
            audio2 = md.listen()
            print(audio2)
            if audio2 == '서울 날씨':
                w_25.get_temperature() #날씨: 서울 위도 경도, 미세먼지 확인 지역
            elif audio2 == '서울 미세먼지':
                w_25.get_tell_pm25() #미세먼지, 지역구 확인 코드
            elif audio2 == '검색': #네이버 검색
                md.speak('어떤걸 검색할까요')
                cd1.search_naver()
            elif audio2 == '음악 검색': #TJ미디어 음악 검색
                md.speak('어떤걸 검색할까요')
                cd1.search_tjsong()
            elif audio2 == '종료':
                break
            else:
                print('오류발생')
                break
    else:
        md.speak('인식하지 못했어요')

except ValueError:
    md.speak('오류발생, 고객센터에 문의하세요')
except md.UnknownValueError:
    print("음성 인식 실패")
except md.RequestError:
    print("서버 에러 발생")
except md.WaitTimeoutError:
    print("인식 실패")