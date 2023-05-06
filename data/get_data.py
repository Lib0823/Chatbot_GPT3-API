from data import weather_data
from data import db_data_manage
import pymongo


# 날씨 데이터 처리.
db_data_manage.weather_deleteData()
db_data_manage.weather_insertData()


# mongoDB data로드
client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["chatbot-data"]
col = db["basic"]

# 데이터 검색 - user, ai
result = col.find({}, {"_id":0, "user":1, "ai":1})

learn_data = []
for data in result:
    learn_data.append(data)

