import os
import openai
from datetime import datetime

ROLE = "user"
openai.api_key = os.getenv("OPENAI_API_KEY")

message = list()
while True:
    input_content = input("질문을 입력해주세요(나가기 : exit) : ")

    if input_content == 'exit':
        break
    
    m = dict()
    m['role'] = ROLE
    m['content'] = input_content
    message.append(m)

    start_time = datetime.now()

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message
    )

    end_time = datetime.now()
    duration = end_time - start_time

    gpt_content = completion.choices[0].message.content
    gpt_role = completion.choices[0].message.role

    m1 = dict()
    m1['role'] = gpt_role
    m1['content'] = gpt_content
    message.append(m1)
    
    print(message)

    with open("response.txt", "a+") as f:
        f.write("\n\n[ USER ]\n")
        f.write(input_content)
        f.write("\n\n[ chatGPT ]\n")
        f.write(gpt_content)
        f.write(f"\n\n걸린 시간 : {duration.total_seconds()}초")
