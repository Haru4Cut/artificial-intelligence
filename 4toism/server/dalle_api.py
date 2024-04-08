from openai import OpenAI
import os

client = OpenAI(api_key = '')


def generate_dalle_image(dalle_prompt, dalle_api_key):

    dalle_response = client.images.generate(
        model="dall-e-3",
        n=1,
        prompt=dalle_prompt,
        size="1024x1024",
        )

    return dalle_response.data[0].url
