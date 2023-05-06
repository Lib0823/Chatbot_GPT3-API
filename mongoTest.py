# import pymongo

# # MongoDB에 연결합니다.
# client = pymongo.MongoClient("mongodb://localhost:27017/")

# # 데이터베이스와 컬렉션을 선택합니다.
# db = client["local"]
# col = db["test1"]


# # 새로운 데이터를 삽입합니다.
# mydict = { "name": "John", "address": "Highway 37" }
# x = col.insert_one(mydict)

# # 삽입한 데이터의 ID를 출력합니다.
# print(x.inserted_id)


# # name이 "John"인 모든 데이터를 검색합니다.
# myquery = { "name": "John" }
# mydoc = col.find(myquery)

# # 검색된 데이터를 출력합니다.
# for data in mydoc:
#     print(data)

    
# # name이 "John"인 모든 데이터를 삭제합니다.
# myquery = { "name": "John" }
# d = col.delete_many(myquery)

# # 삭제된 데이터의 수를 출력합니다.
# print(d.deleted_count)



