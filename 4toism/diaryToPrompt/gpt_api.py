from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_gpt_prompt(user_diary):
    gpt_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assisatant who writes a simple description that describes a picture based on the user's input in English."},
            {"role": "user", "content": f"{user_diary[0]}, {user_diary[1]}, {user_diary[2]}"}
            ]
        )

    # print(gpt_response.choices[0].message.content)

    return gpt_response.choices[0].message.content
