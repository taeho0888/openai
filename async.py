import os
import openai
from datetime import datetime
import asyncio
import aiohttp
import certifi
import ssl

class ChatBot:
    ROLE = "user"
    MODEL = "gpt-3.5-turbo"

    def __init__(self):
        self.openai = openai
        self.openai.api_key = os.getenv("OPENAI_API_KEY")
        self.messages = []

    async def ask_question(self, question):
        message = {
            'role': ChatBot.ROLE,
            'content': question
        }
        self.messages.append(message)
        return await self.get_response()

    async def get_response(self):
        start_time = datetime.now()
        
        ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        ssl_context.load_verify_locations(cafile=certifi.where())

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
            url = f"https://api.openai.com/v1/engines/{ChatBot.MODEL}/completions"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.openai.api_key}",
            }
            payload = {
                "messages": self.messages
            }

            async with session.post(url, json=payload, headers=headers) as resp:
                completion = await resp.json()
        
        end_time = datetime.now()
        duration = end_time - start_time
        response = completion['choices'][0]['message']
        self.messages.append(dict(response))
        print(response['content'])
        
        return response['content'], duration.total_seconds()

    def save_to_file(self, filename, question, response, duration):
        with open(filename, "a+") as f:
            f.write("\n\n[ USER ]\n")
            f.write(question)
            f.write("\n\n[ chatGPT ]\n")
            f.write(response)
            f.write(f"\n\n걸린 시간 : {duration}초")

async def main():
    chat_bot = ChatBot()

    while True:
        input_content = input("질문을 입력해주세요(나가기 : exit) : ")

        if input_content == 'exit':
            break

        response, duration = await chat_bot.ask_question(input_content)
        chat_bot.save_to_file("response.txt", input_content, response, duration)
        # print(response)

if __name__ == '__main__':
    asyncio.run(main())
