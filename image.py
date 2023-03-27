import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
image = openai.Image.create(
  prompt="app icon of grape farm",
  n=2,
  size="1024x1024"
)
print(image)