from dotenv import load_dotenv
import os
import openai
import requests

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
data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Hello!"}],
}
response = requests.post(url, headers=headers, json=data)

# 결과 확인
print(response.json())