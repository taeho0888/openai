import os
import openai
from datetime import datetime

class ChatBot:
    ROLE = "user"
    MODEL = "gpt-3.5-turbo"

    def __init__(self):
        self.openai = openai
        self.openai.api_key = os.getenv("OPENAI_API_KEY")
        self.messages = []

    def ask_question(self, question):
        message = {
            'role': ChatBot.ROLE,
            'content': question
        }
        self.messages.append(message)
        return self.get_response()

    def get_response(self):
        start_time = datetime.now()
        completion = self.openai.ChatCompletion.create(
            model=ChatBot.MODEL,
            messages=self.messages
        )
        end_time = datetime.now()
        duration = end_time - start_time
        response = completion.choices[0].message
        self.messages.append(dict(response))
        print(response.content)
        
        return response.content, duration.total_seconds()

    def save_to_file(self, filename, question, response, duration):
        with open(filename, "a+") as f:
            f.write("\n\n[ USER ]\n")
            f.write(question)
            f.write("\n\n[ chatGPT ]\n")
            f.write(response)
            f.write(f"\n\n걸린 시간 : {duration}초")

def main():
    chat_bot = ChatBot()

    while True:
        input_content = input("질문을 입력해주세요(나가기 : exit) : ")

        if input_content == 'exit':
            break

        response, duration = chat_bot.ask_question(input_content)
        chat_bot.save_to_file("response.txt", input_content, response, duration)
        # print(response)

if __name__ == '__main__':
    main()
