import speech_recognition as sr
import module1 as md
import search_code1 as cd1
r = sr.Recognizer() # 인식을 위한 객체 생성
mic = sr.Microphone() # 마이크 사용을 위한 객체 생성

with mic as source: # 마이크에 담긴 소리를 토대로 아래 코드 실행
    r.adjust_for_ambient_noise(source)# 잡음 제거 코드 (없어도 무방)
    print('음성을 입력하세요, <시리야>')
    audio1 = r.listen(source) # 해당 소리를 오디오 파일 형태로 변환
    try:
        result1 = r.recognize_google(audio1, language = "ko-KR") # 오디오를 토대로 음성 인식
        print('결과: ' + result1) # 인식 결과 출력
        if result1 == '시리야':
            while True:
                r.adjust_for_ambient_noise(source)  # 잡음 제거 코드 (없어도 무방)
                md.speak('원하는 결과를 말씀해주세요. 1. 서울 날씨, 2. 서울 미세먼지, 3. 검색, 4. 종료')
                audio2 = r.listen(source, phrase_time_limit=3)
                try:
                    result2 = r.recognize_google(audio2, language="ko-KR")# 오디오를 토대로 음성 인식
                    print(result2)
                    if result2 == '서울 날씨':
                        md.weather_pm25(37.56, 126.76, '서울').get_weather() #print('결과: ' + result2)  # 인식 결과 출력
                    elif result2 == '서울 미세먼지':
                        md.weather_pm25(37.56, 126.76, '서울').get_pm25weather()
                    elif result2 == '검색':
                        md.speak('어떤걸 검색할까요')
                        cd1.search_keyword()
                    elif result2 == '종료':
                        break
                    else:
                        print('오류발생')
                except sr.UnknownValueError:
                    print("음성 인식 실패")
                except sr.RequestError:
                    print("서버 에러 발생")
                except sr.WaitTimeoutError:
                    print("인식 실패")
    except sr.UnknownValueError:
        print("음성 인식 실패")
    except sr.RequestError:
        print("서버 에러 발생")
    except sr.WaitTimeoutError:
        print("인식 실패")