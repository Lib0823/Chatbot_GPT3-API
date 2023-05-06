from utils import Api_key
from data import time_data
import requests
import json

try:
    # 초단기 실황
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
    params = {
        'serviceKey': Api_key.weather_key,
        'pageNo': '1',
        'numOfRows': '30',
        'dataType': 'JSON',
        'base_date': str(time_data.getDate()),
        'base_time': str(time_data.getTime()),
        'nx': '54',
        'ny': '124'
    }
    # 강수 형태 - PTY
    # 기온 - T1H
    response = requests.get(url, params=params)

    # JSON 데이터를 파이썬 객체로 변환
    data = json.loads(response.text)

    # "item" 목록에서 "category"가 "T1H"인 라인을 찾아 "obsrValue" 값을 추출
    t1h_item = next(item for item in data['response']['body']['items']['item']
                    if item['category'] == 'T1H')
    t1h_value = t1h_item['obsrValue'] + "도"

    # "item" 목록에서 "category"가 "PTY"인 라인을 찾아 "obsrValue" 값을 추출
    pty_item = next(item for item in data['response']['body']['items']['item']
                    if item['category'] == 'PTY')
    pty_value = pty_item['obsrValue']

    # "item" 목록에서 "category"가 "WSD"인 라인을 찾아 "obsrValue" 값을 추출
    wsd_item = next(item for item in data['response']['body']['items']['item']
                    if item['category'] == 'WSD')
    wsd_value = wsd_item['obsrValue']

    #print(t1h_value)
    t1h = t1h_value

    # [강수 형태] 없음(0), 비(1), 비/눈(2), 눈(3), 빗방울(5), 빗방울눈날림(6), 눈날림(7)
    if pty_value == '0':
        pty = '맑음'
    elif pty_value == '1':
        pty = '비'
    elif pty_value == '2':
        pty = '비'
    elif pty_value == '3':
        pty = '눈'
    elif pty_value == '5':
        pty = '빗방울'
    elif pty_value == '6':
        pty = '빗방울'
    elif pty_value == '7':
        pty = '눈날림'
    else:
        pty = '정보없음'

    # [풍속]
    if float(wsd_value) <= 3.3:
        wsd = '미풍'
    elif float(wsd_value) <= 5.4:
        wsd = '약풍'
    elif float(wsd_value) <= 10.7:
        wsd = '중풍'
    elif float(wsd_value) <= 17.1:
        wsd = '강픙'
    else:
        wsd = '위험'
        
except:
    print("weather_data Error")
    t1h = "현재 기온 정보를 알 수 없습니다."
    pty = "현재 날씨 정보를 알 수 없습니다."
    wsd = "현재 바람 정보를 알 수 없습니다."


