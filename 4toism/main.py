import os
import pandas as pd
os.environ["OPENAI_API_KEY"] = 'api_key' # api key

from gpt_api import generate_gpt_prompt
from dalle_api import generate_dalle_image

def main():
    diary_lst = [""] # Create a cute and funny 8k webtoon style illustration : With a friend, today I went to see a movie. We enjoyed an exciting action movie and lost track of time. In the end, we finished the day by eating delicious food together. Place: Movie theater.
    # 사용자로부터 일기 입력 받기
    user_diary = input("일기를 입력하세요: ")

    # GPT API를 사용하여 입력을 DALL-E 프롬프트 형식으로 변경
    dalle_prompt = generate_gpt_prompt(user_diary.split('/'))
    
    # DALL-E API를 사용하여 이미지 생성
    dalle_api_key = os.environ.get("OPENAI_API_KEY")
    generated_image_url = generate_dalle_image(dalle_prompt, dalle_api_key)

    # 생성된 이미지 URL 출력
    print("생성된 이미지:", generated_image_url)

# AI에서 gpt prompt 생성
def gpt_api(diary_input, character_input):
    from openai import OpenAI
    client = OpenAI()
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    completion = client.chat.completions.create(
    model="ft:gpt-3.5-turbo-0613:personal:prompt-train-val-1:93Iduhnt",
    messages=[
        # 모델에 system 명령과 사용자 입력 전달
        {"role": "system", "content": "You are an assistant who creates a 'dalle' prompt based on the user's diary written according to 'who with', 'what', and 'where'."},
        {"role": "user", "content": diary_input}
    ]
    )
    dalle_prompt = completion.choices[0].message.content + character_input
    print(dalle_prompt)

    # DALL-E API를 사용하여 이미지 생성
    dalle_api_key = os.environ.get("OPENAI_API_KEY")
    generated_image_url = generate_dalle_image(dalle_prompt, dalle_api_key)

    # 생성된 이미지 URL 출력
    print("생성된 이미지:", generated_image_url)

if __name__ == "__main__":
    gpt_api()
