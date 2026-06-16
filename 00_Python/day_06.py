from dotenv import load_dotenv
print(load_dotenv())

from utils import call_llm, mask_pii, is_harmfull

questions = input("Enter your question : ")


prompt = f"""
Your are helpfull assistant for the user. Reply in polite way 
Questions : {questions}
"""

# print(prompt)

if is_harmfull(prompt):
    print("Your question is harmfull")
else:
    # updated_prompt = mask_pii(prompt)
    # print('here is my updated prompt',updated_prompt)
    response = call_llm(prompt)
    print(response)

