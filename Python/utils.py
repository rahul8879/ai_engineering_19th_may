

from dotenv import load_dotenv
print(load_dotenv())
from openai import OpenAI
import json
import re

harmfull_word= ['harsh', 'bad', 'badly','destroy']

def is_harmfull(prompt):
    words = prompt.lower().split()
    for word in words:
        if word in harmfull_word:
            return True
    

def mask_pii(prompt):
    """
    This function will mask the PII in the prompt
    """

    updated_prompt = re.findall(r'\d{10}', prompt)
    print(updated_prompt)
    prompt = prompt.replace(updated_prompt[0], len(updated_prompt[0])*'#')

    return prompt

client = OpenAI()
def call_llm(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    ).choices[0].message.content
    return response


def product_number(a,b):

    return a*b

print(product_number(2))