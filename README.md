<h1>※Learnable Chatbot API※</h1>

<h3>프로젝트에 필요한 데이터를 학습시켜 사용 가능한 챗봇 API입니다.</h3>
<br>
<b>개요</b><br>
<p>⭕PAE, MiracleStep, WorkingMate 등의 프로젝트를 진행하던 중 개발이 완료된 후 유지보수 시에 각 프로젝트에서 필요한 정보들이 학습된 챗봇이 있으면 간단한 문제는 쉽고 빠르게 해결할 수 있며, 사용자 입장에서도 바로바로 답변 받을 수 있기 때문에 편리할 것 같다고 생각하여 각각의 필요한 정보들을 간단하게 학습시켜 사용할 수 있도록 API를 구성함.</p>
<br>
<b>특징</b><br>
<p>⭕openAI사의 GPT-2 모델 활용. (3, 4 모델은 개인 학습 불가)</p>
<p>⭕Data파일에 Json타입으로 원하는 데이터를 추가하여 학습</p>
<p>⭕사용 프로젝트에 맞게 이름, 형식 등 세팅값 조정 가능</p>
<p>⭕기상청의 openAPI를 사용하여 현재 날씨정보를 자동으로 학습</p>
<br>
<b>기술</b><br>
<p>⭕Python으로 GTP-2모델 학습 및 처리</p>
<p>⭕Flask Web Framework를 활용하여 API구현</p>
<p>⭕goormIDE의 컨테이너에서 동작시켜 외부에서 Domain(url)을 사용하여 호출 가능</p>
<br>
<b>사용 방법</b><br>
<p>1️⃣ application.py 파일의 <i>openai.api_key = ""</i> 부분을 자신의 API키로 변경</p>
<p>2️⃣ 학습 시키고자 하는 내용을 chatbot_data.json 파일에 Json형식으로 추가하여 저장</p>
<p>3️⃣ application.py와 chatbot_data.json파일을 서버에 올린다 (goormIDE)</p>
<p>[호출]</p>
<p>4️⃣ 외부에서 해당 코드 작성</p>
import requests<br>
import json<br>
url = 'https://chatbot-api.run.goorm.site/'<br>
headers = {'Content-Type': 'application/json'}<br>
data = {'user_input': '안녕'}<br>
response = requests.post(url, headers=headers, data=json.dumps(data))<br>
print(response.json())<br>	
![image](https://user-images.githubusercontent.com/89591782/230947470-0b7da05a-4ca4-4143-b3c1-c5888f3560a6.png)
<br><br>
<p>5️⃣ URL수정 및 data에 'user_input' : '???' 질문 내용 입력하여 API호출.</p>

<br><br>
```
┌───────────────────────────────────────────────┐
   __ _  ___   ___  _ __ _ __ ___   (_) ___  
    / _` |/ _ \ / _ \| '__| '_ ` _ \  | |/ _ \ 
   | (_| | (_) | (_) | |  | | | | | |_| | (_) |
    \__, |\___/ \___/|_|  |_| |_| |_(_)_|\___/ 
    |___/                                      
			     🌩 𝘼𝙣𝙮𝙤𝙣𝙚 𝙘𝙖𝙣 𝙙𝙚𝙫𝙚𝙡𝙤𝙥!
└───────────────────────────────────────────────┘
```
