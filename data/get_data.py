from data import db_data_manage
import pymongo


# 날씨 데이터 처리.
def process_weather():
    db_data_manage.weather_deleteData()
    db_data_manage.weather_insertData()

# DB 데이터 검색
def get_data(col_name):
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    db = client["chatbot-data"]
    col = db[col_name]

    result = col.find({}, {"_id":0, "user":1, "ai":1})

    learn_data = []
    for data in result:
        learn_data.append(data)
        
    return learn_data

