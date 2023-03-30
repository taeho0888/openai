import os
import openai

input = input("무슨 이미지를 출력할까요? : ")
openai.api_key = os.getenv("OPENAI_API_KEY")
image = openai.Image.create(
  prompt=input,
  n=2,
  size="1024x1024"
)
print(image)