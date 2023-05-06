from data import weather_data
import pymongo

# 날씨 데이터 관리
# - 이전 날씨 데이터를 삭제하고 현재 데이터 삽입

# mongoDB data로드.
client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["chatbot-data"]
col = db["basic"]

user_query = ['현재 기온', '현재 날씨', '현재 바람']

def weather_deleteData():
    # 이전 값 DELETE
    cnt_x = 0
    for d in user_query:
        x = col.delete_many({"user": d})
        cnt_x += x.deleted_count

    # 값 삭제 체크
    if cnt_x >= 3:
        print("weather_del Ok")
    else:
        print("weather_del Error") 
        

def weather_insertData():
    # 현재 값 INSERT
    data = []

    data.append({ 
        "user": user_query[0], # 현재 기온
        "ai": weather_data.t1h
    })
    data.append({
        "user": user_query[1], # 현재 날씨
        "ai": weather_data.pty
    })
    data.append({
        "user": user_query[2], # 현재 바람
        "ai": weather_data.wsd
    })

    for i in data:
        col.insert_one(i)


    # 값 삽입 체크
    if len(data) == 3:
        print("weather_in Ok")
    else:
        print("weather_in Error")











