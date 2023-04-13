from key import api_key
from config import *
from Train_gpt2 import learn_data

from flask import Flask, request, jsonify, render_template

import sys
import openai
import json

application = Flask(__name__)

# 기본 세팅값
openai.api_key = api_key

self.model_engine = model_engine
self.temperature = temperature
self.max_tokens = max_tokens


# chat_data 로드
with open("chatbot_data.json", "r") as f:
    chat_data = json.load(f)


# 챗봇 API 매핑 (POST)
@application.route("/", methods=['POST'])
def chatbot():
    try:
        request_data = request.get_json()
        user_input = request_data['user_input']
        response = learn_data(chat_data + [{"user": user_input, "ai": ""}])
        return jsonify({"racle": response})
    
    except:
        return jsonify({"error": "네트워크에 문제가 발생했습니다. 다시 시도해주세요."})


# 도움말 및 설명
@application.route("/help")
def chatbot-help1():
    return render_template('help.html')
    

# 앱 실행
if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(sys.argv[1]))
    
    