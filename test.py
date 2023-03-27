from dotenv import load_dotenv
import os
import openai
import requests
from datetime import datetime

# .env 파일 로드
load_dotenv()

openai.organization = "org-wQ10XrNn2gKCe2xI1QhDtWUZ"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()

# API 요청 보내기
url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai.api_key}",
}


while True:
    input_content = input("질문을 입력해주세요(나가기 : exit) : ")
    if input_content == "exit":
        break

    data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "teacher", "content": input_content}],
    }
    
    start_time = datetime.now()
    response = requests.post(url, headers=headers, json=data)
    end_time = datetime.now()
    duration = end_time - start_time

    response_json = response.json()
    content = response_json["choices"][0]["message"]["content"]

    with open("response.txt", "a+") as f:
        f.write("\n\n[ USER ]\n")
        f.write(input_content)
        f.write("\n\n[ chatGPT ]\n")
        f.write(content)
        f.write(f"\n\n걸린 시간 : {duration.total_seconds()}초")
