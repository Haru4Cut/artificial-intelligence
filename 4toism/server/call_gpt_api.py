from openai import OpenAI
from gpt_api import generate_gpt_prompt

class haruFour:
    # AI에서 gpt prompt 생성
    def __init__(self) -> None:
        self.client = OpenAI(api_key='') # api key

    def gpt_api(self, diary_keywords):
        diary_input = f"누구랑:{diary_keywords[0]}/무엇을:{diary_keywords[2]}/어디서:{diary_keywords[1]}/감정:{diary_keywords[3]}"

        completion = self.client.chat.completions.create(
        # model="ft:gpt-3.5-turbo-0613:personal:prompt-train-val-1:93Iduhnt",
        model = "ft:gpt-3.5-turbo-0613:personal:try2:908MV90a",
        messages=[
            # 모델에 system 명령과 사용자 입력 전달
            {"role": "system", "content": "You are an assistant who creates a 'dalle' prompt based on the user's diary written according to 'who with', 'what', and 'where'."},
            {"role": "user", "content": diary_input}
        ]
        )
        dalle_prompt = completion.choices[0].message.content
        dalle_prompt += ''
        return dalle_prompt

    