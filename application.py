from utils import Api_key
from data import get_data
from learning import model_training
from pymongo import MongoClient

from flask import Flask, request, jsonify, render_template
from flask_apscheduler import APScheduler
import sys
import openai

# key
openai.api_key = Api_key.openAI_key


application = Flask(__name__)
scheduler = APScheduler()

# Flask 앱 설정
application.config['SCHEDULER_API_ENABLED'] = True
application.config['JOBS'] = [
    {
        'id': 'weather_update',
        'func': get_data.process_weather,
        'trigger': 'interval',
        'hours': 0.5
    }
]

# json [] 사용해서 제목과 url제공
# ex> user : 지원정보1, ai : [지원프로그램제목, 사이트URL]

# API mapping(POST) - basic
@application.route("/", methods=['POST'])
def chatbot_basic():
    try:    
        request_data = request.get_json()
        user_input = request_data['user_input']

        # DB 학습 데이터 받아옴
        col_name = "basic"
        learn_data = get_data.get_data(col_name)

        response = model_training(learn_data + [{"user": user_input, "ai": ""}])
        return jsonify({"basic": response})
    except Exception as e:
        # 에러 처리
        error_code = getattr(e, "code", None)
        if error_code:
            # 에러 코드 사용
            # 원하는 작업 수행
            return jsonify({"error": f"Error code: {error_code}"})
        else:
            # 에러 코드가 없는 경우
            # 기본적인 에러 처리
            return jsonify({"error": "네트워크에 문제가 발생했습니다."})
        
# API mapping(POST) - pae
@application.route("/pae", methods=['POST'])
def chatbot_pae():
    try:    
        request_data = request.get_json()
        user_input = request_data['user_input']

        # DB 학습 데이터 받아옴
        col_name = "pae"
        learn_data = get_data.get_data(col_name)

        response = model_training(learn_data + [{"user": user_input, "ai": ""}])
        return jsonify({"pae": response})
    except:
        return jsonify({"error": "네트워크에 문제가 발생했습니다. 다시 시도해주세요."})

# API mapping(POST) - pae (consult)
@application.route("/pae/consult", methods=['POST'])
def chatbot_pae_consult():
    try:    
        request_data = request.get_json()
        user_input = request_data['user_input']

        # DB 학습 데이터 받아옴
        col_name = "pae_consult"
        learn_data = get_data.get_data(col_name)

        response = model_training(learn_data + [{"user": user_input, "ai": ""}])
        return jsonify({"pae_consult": response})
    except:
        return jsonify({"error": "네트워크에 문제가 발생했습니다. 다시 시도해주세요."})

# API mapping(POST) - working mate
@application.route("/wm", methods=['POST'])
def chatbot_wm():
    try:    
        request_data = request.get_json()
        user_input = request_data['user_input']

        # DB 학습 데이터 받아옴
        col_name = "wm"
        learn_data = get_data.get_data(col_name)

        response = model_training(learn_data + [{"user": user_input, "ai": ""}])
        return jsonify({"wm": response})
    except:
        return jsonify({"error": "네트워크에 문제가 발생했습니다. 다시 시도해주세요."})

# API mapping(POST) - working mate (exercise)
@application.route("/wm/exercise", methods=['POST'])
def chatbot_wm_exercise():
    try:    
        request_data = request.get_json()
        user_input = request_data['user_input']

        # DB 학습 데이터 받아옴
        col_name = "wm_exercise"
        learn_data = get_data.get_data(col_name)

        response = model_training(learn_data + [{"user": user_input, "ai": ""}])
        return jsonify({"wm_exercise": response})
    except:
        return jsonify({"error": "네트워크에 문제가 발생했습니다. 다시 시도해주세요."})

# API mapping(POST) - miracle step
@application.route("/ms", methods=['POST'])
def chatbot_ms():
    try:    
        request_data = request.get_json()
        user_input = request_data['user_input']

        # DB 학습 데이터 받아옴
        col_name = "ms"
        learn_data = get_data.get_data(col_name)

        response = model_training(learn_data + [{"user": user_input, "ai": ""}])
        return jsonify({"ms": response})
    except:
        return jsonify({"error": "네트워크에 문제가 발생했습니다. 다시 시도해주세요."})

# API mapping(POST) - piuda
@application.route("/piuda", methods=['POST'])
def chatbot_piuda():
    try:    
        request_data = request.get_json()
        user_input = request_data['user_input']

        # DB 학습 데이터 받아옴
        col_name = "piuda"
        learn_data = get_data.get_data(col_name)

        response = model_training(learn_data + [{"user": user_input, "ai": ""}])
        return jsonify({"piuda": response})
    except Exception as e:
        # 에러 처리
        error_code = getattr(e, "code", None)
        return jsonify({"piuda": response})

    

# 도움말 및 설명
@application.route("/help")
def chatbot_help():
    return render_template('help.html')

    
# 앱 실행
if __name__ == "__main__":
    # 스케줄러 시작
    scheduler.init_app(application)
    scheduler.start()
    
    application.debug = True
    application.run(host='0.0.0.0', port=int(sys.argv[1]))

    

