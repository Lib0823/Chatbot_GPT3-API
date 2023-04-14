from utils import Api_key
from data import get_data
from learning import learn_data

from flask import Flask, request, jsonify, render_template

import sys
import openai
import json

application = Flask(__name__)

# key
openai.api_key = Api_key.openAI_key


# 챗봇 API 매핑 (POST)
@application.route("/", methods=['POST'])
def chatbot():
    try:
        request_data = request.get_json()
        user_input = request_data['user_input']
        response = learn_data(get_data.learn_data + [{"user": user_input, "ai": ""}])
        return jsonify({"racle": response})
    
    except:
        return jsonify({"error": "네트워크에 문제가 발생했습니다. 다시 시도해주세요."})


# 도움말 및 설명
@application.route("/help")
def chatbot_help():
    return render_template('help.html')
    

# 앱 실행
if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0', port=int(sys.argv[1]))
    
    