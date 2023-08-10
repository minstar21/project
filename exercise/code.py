import json
import requests
from bs4 import BeautifulSoup
import module1 as md
import speech_recognition as sr
from gtts import gTTS
import playsound
import os

def speak(text):
	tts = gTTS(text=text, lang='ko')
	tts.save('voice.mp3')
	playsound.playsound('voice.mp3')
	os.remove('voice.mp3')

def listen():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:  # 마이크에 담긴 소리를 토대로 아래 코드 실행
        audio = r.listen(source,phrase_time_limit=3)  # 해당 소리를 오디오 파일 형태로 변환
        result = r.recognize_google(audio, language="ko-KR")  # 오디오를 토대로 음성 인식
        speak(result)
    return result


----
try:
    audio_x = int(listen())
    for airinfo in airinfo_list:
        result_list.append([airinfo['sidoName'], airinfo['stationName'], airinfo['pm25Value'], airinfo['pm25Grade'],
                            airinfo['dataTime']])
    speak('도시명, 지역구 코드, 미세먼지농도, 미세먼지등급, 현재시간을 알려드릴께요')
    for i in result_list[audio_x]:
        speak(i)
    speak('입니다')
except:
    speak('잘못된 코드를 입력하셨습니다')