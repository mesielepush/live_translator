from dotenv import load_dotenv
import os
import openai
load_dotenv('.env')
import time
from datetime import datetime
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_translation(text_to_translate, output_language):
    user = f'Translate the following text into {output_language}'
    response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
             messages=[
                        #{"role": "system", "content": f'you are a {output_language} translator'},
                         {'role': 'assistant','content': text_to_translate.capitalize()},
                        {"role": "user", "content": user},

                    ],
            temperature = 0,
            max_tokens=None
        )
    return response['choices'][0]['message']['content']