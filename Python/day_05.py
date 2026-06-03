
output = ['Billing | 0.9', 'Technical | 0.8', 'General | 0.7']

category =[]
score = []
for i in output:
    cat = i.split('|')[0].strip()
    conf = float(i.split('|')[1].strip())
    category.append(cat)
    score.append(conf)

print(category)
print(score)



emails = [
    {
        "body": "Help me to resolve my billing issue",
        "subject": "facing issue"
    },
    {
        "body": "I am facing a technical issue with my account",
        "subject": "facing issue"
    },
    {
        "body": "I have a general inquiry about your services",
        "subject": "general inquiry"
    },
    {
        "body": "I have a billing issue",
        "subject": "billing issue"
    }
]


from dotenv import load_dotenv
print(load_dotenv())
from openai import OpenAI
import json

# with open("test_emails.json", "r") as f:
#     emails = json.load(f)
# print(len(emails))

client = OpenAI()
# for i in emails:
#      prompt = f"""classify below email into one of the categories
#         - Billing issue
#         - Technical issue
#         - General inquiry
#         and also give me score between 0-10 and make sure it should be only in number 
#         0 - no confidence
#         5 - some confidence
#         10 - full confidence
#         Your output should be exactly Category | Score
#         email : {i['body']}
#         subject : {i['subject']}
#         """
     
#      response = client.chat.completions.create(
#                 model="gpt-4o",
#                 messages=[
#                     {
#                         "role": "user",
#                         "content": prompt
#                     }
#                 ]
#             ).choices[0].message.content
#      category= response.split("|")[0].strip()
#      confidence = float(response.split("|")[1].strip())
#      i['category'] = category
#      i['confidence'] = confidence

# print(emails)


# import json 

# with open("llm_output.json", "w") as f:
#     json.dump(emails, f)


with open("dummy.txt", "r") as f:
    blogs = f.readlines()

# print(blogs)

prompt = f"""
Reply based on context only

Context:
{''.join(blogs)}
Question: Who is Rahul Tiwari?
"""

print(len(prompt))


response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            ).choices[0].message.content

print(response)

# result = output.split('|')
# category = result[0].strip()
# confidence = float(result[1].strip())

# print(f"Category: {category}, Confidence: {confidence}")


# result = output.split('|')
# print(result)
# print(result[0].split(',')[0])