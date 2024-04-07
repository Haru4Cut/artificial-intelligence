from openai import OpenAI
import os
os.environ["OPENAI_API_KEY"] = '' # api key

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_gpt_prompt(character_input):
    gpt_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assisatant who writes a simple description that describes a picture based on the user's input."},
            {"role": "user", "content": character_input}
            ]
        )

    # print(gpt_response.choices[0].message.content)

    return gpt_response.choices[0].message.content