import datetime
import pytz

# 날짜 반환
def getDate():
    # 지역 세팅
    mytz = pytz.timezone('Asia/Seoul')

    # 현재 시간
    now = datetime.datetime.now(mytz)

    return now.today().strftime("%Y%m%d")
    
# 시간 반환
def getTime():
    # 지역 세팅
    mytz = pytz.timezone('Asia/Seoul')

    # 현재 시간
    now = datetime.datetime.now(mytz)
    
    # 기상청 데이터 약 3~40분 딜레이가 발생하여 1시간 지연시킨다.
    hour = now.hour - 1

    # 시간이 한 자릿수면 앞에 '0'붙임
    if hour < 10:
        hour = "0"+str(hour)
    
    
    # 기상청 데이터가 30분 단위로 올라온다.
    minute = "00"
    if now.minute > 30:
        minute = "30"
        
        
    time = str(hour) + minute

    return time


