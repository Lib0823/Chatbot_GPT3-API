from data import weather_data
import json

# chat_data 로드
with open("data/chatbot_data.json", "r") as f:
    file_data = json.load(f)
    

# 날씨 정보 추가 학습
file_data.append(weather_data.t1h_data)
file_data.append(weather_data.pty_data)
file_data.append(weather_data.wsd_data)

    
learn_data = file_data
print(learn_data)
