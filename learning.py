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
def model_training(chat_data):
    inputValue = ""
    for chat in chat_data:
        inputValue += f"User: {chat['user']}\nAI: {chat['ai']}\n"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=inputValue,
        temperature=temperature,
        max_tokens=max_tokens,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

