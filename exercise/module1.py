import json
import requests
from gtts import gTTS
import playsound
import os
import pandas as pd
import speech_recognition as sr
r = sr.Recognizer() # 인식을 위한 객체 생성
mic = sr.Microphone() # 마이크 사용을 위한 객체 생성

def speak(text): #말하기 함수
	tts = gTTS(text=text, lang='ko')
	tts.save('voice.mp3')
	playsound.playsound('voice.mp3')
	os.remove('voice.mp3')

def listen(): #듣기 함수, 구글 크롬 엔진 사용
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:  # 마이크에 담긴 소리를 토대로 아래 코드 실행
        audio = r.listen(source,phrase_time_limit=3)  # 해당 소리를 오디오 파일 형태로 변환
        try:
            result = r.recognize_google(audio, language="ko-KR")  # 오디오를 토대로 음성 인식
        except sr.UnknownValueError:
            print("음성 인식 실패")
        except sr.RequestError:
            print("서버 에러 발생")
        except sr.WaitTimeoutError:
            print("인식 실패")
    return result
#pip install playsound == 1.2.2 버전으로 다운그레이드하니 해결




from bs4 import BeautifulSoup
class weather_pm25: #weather_pm25(위도, 경도, 서울) 입력

    def __init__(self, latitude, longitude, sidoName):
        self.latitude = latitude
        self.longitude = longitude
        self.sidoName = sidoName

    # 1. 현재 실시간 날씨, 실시간 미세먼지 정보 불러오기
    def get_temperature(self): #서울 현재 온도
        url = f'https://api.open-meteo.com/v1/forecast?latitude={self.latitude}&longitude={self.longitude}&current_weather=true&timezone=auto'
        response = requests.get(url)
        json_data = json.loads(response.text)
        speak(str(json_data["current_weather"]['temperature']))

    def get_tell_pm25(self): #미세먼지25 정보 출력
        params = {
            'serviceKey': 'dFIHe0liJzwfyJHUvf1BDJoJbvGh4AoCY9PSIr1n4x1txxNeZO7gXSoAPXEAGfbcXUUMwdC4DJmIw/8ldBCN6A==',
            'returnType': 'json',
            'numOfRows': '100',
            'pageNo': '1',
            'sidoName': self.sidoName,
            'ver': '1.0', }

        response = requests.get('http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty',
                                params=params)
        json_data = json.loads(response.text)
        airinfo_list = json_data['response']['body']['items']
        result_list = [] #공공개방포탈 원하는 날씨 정보 추출
        speak('원하는 지역구 코드(숫자0~39)를 입력해주세요: 중랑구(36)')
        try:
            audio_x = int(listen())

            for airinfo in airinfo_list:
                result_list.append([airinfo['sidoName'], airinfo['stationName'], airinfo['pm25Value'], airinfo['pm25Grade'],
                                    airinfo['dataTime']])
                #result_list 내 None값으로 인한 speak함수 출력 오류 방지(list -> df.fillna -> list)
                result_list = pd.DataFrame(result_list).fillna('없음').values.tolist()
            speak('도시명, 지역구 코드, 미세먼지농도, 미세먼지등급, 현재시간을 알려드릴께요')
            for i in result_list[audio_x]:
                speak(i)
            speak('입니다')
        except ValueError:
            speak('코드입력이 잘못되었습니다 다시 시도해주세요')