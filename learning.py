from utils import config
from flask import Flask, request, jsonify, render_template

import sys
import openai
import json

# 세팅값 가져오기
model_engine = config.model_engine
temperature = config.temperature
max_tokens = config.max_tokens


# 데이터 학습시키기
def learn_data(chat_data):
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

