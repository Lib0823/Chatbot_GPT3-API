from flask import Flask, request, jsonify
import sys
import openai
import json

application = Flask(__name__)

# 기본 세팅값
openai.api_key = "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"

model_engine = "text-davinci-002"
temperature = 0.7
max_tokens = 100


# chat_data 로드
with open("chatbot_data.json", "r") as f:
    chat_data = json.load(f)


# 데이터 학습시키기
def train_gpt2(chat_data):
    prompt = ""
    for chat in chat_data:
        prompt += f"User: {chat['user']}\nAI: {chat['ai']}\n"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()


# # 디폴트 매핑
# @application.route("/")
# def hello():
#     return "Hello, Inbeom's ChatBot-API!"

# 챗봇 API 매핑 (POST)
@application.route("/", methods=['POST'])
def chatbot():
    try:
        request_data = request.get_json()
        user_input = request_data['user_input']
        response = train_gpt2(chat_data + [{"user": user_input, "ai": ""}])
        return jsonify({"racle": response})
    except:
        return jsonify({"error": "네트워크에 문제가 발생했습니다. 다시 시도해주세요."})


# 앱 실행
if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(sys.argv[1]))
    
    
    
# # 해당 API 호출 시 사용 코드
# # *주의사항* -> header에 json타입 명시, data를 json타입으로 dumps()하여 body에 담아 전달.

# import requests
# import json

# url = 'https://chatbot-api.run.goorm.site/'
# headers = {'Content-Type': 'application/json'}
# data = {'user_input': 'chatbot-API 개발 성공,, ㅅㅂ '}

# response = requests.post(url, headers=headers, data=json.dumps(data))
# print(response.json())
