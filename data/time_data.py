import datetime
import pytz
import time

# 날짜 반환
def gDate():
    # 지역 세팅
    mytz = pytz.timezone('Asia/Seoul')

    # 현재 시간
    now = datetime.datetime.now(mytz)

    return now.today().strftime("%Y%m%d")
    
# 시간 반환
def gTime():
    # 지역 세팅
    mytz = pytz.timezone('Asia/Seoul')

    # 현재 시간
    now = datetime.datetime.now(mytz)
    
    # 기상청 데이터 약 3~40분 딜레이가 발생하여 1시간 지연시킨다.
    hour = now.hour - 1
    
    
    # 기상청 데이터가 30분 단위로 올라온다.
    minute = "00"
    if now.minute > 30:
        minute = "30"
        
        
    time = str(hour) + minute

    return time


