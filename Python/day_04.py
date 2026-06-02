# prompt ="""Hi, How are you
# Please help me to generate the python code
# fsfsdf

# fsdfs

# sdfgsdf
# fsdf

# sfsd

# """

# print(type(prompt))
# print(prompt[0:7])

# multipline string
# prompt = """Hi, How are you
# Please help me to generate the python code

# """

# print(type(prompt))

name = 'rahul'

# if name.lower() == 'Rahul'.lower():
#     print("Hello Rahul!")

# else:
#     print("Hello Guest!")

# prompt = "Hi test something"
# print(len(prompt))

# operation with string 
# v1= 'Rahul'
# v2= 'Sharma'
# sep = '?'

# print(v1+sep+v2+' hello')
from dotenv import load_dotenv

print(load_dotenv())


from openai import OpenAI
client = OpenAI()

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


output = []
for i in emails:
    # print(i['subject'])
    prompt = f"""classify below email into one of the categories
        - Billing issue
        - Technical issue
        - General inquiry
        Just return the category no extra explanation
        email : {i['body']}
        subject : {i['subject']}
        """
    # print(prompt)
    print("###"*50)

    response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
).choices[0].message.content
    output.append(response)

print(output)


# response = client.chat.completions.create(
#     model="gpt-4",
#     messages=[
#         {
#             "role": "user",
#             "content": prompt
#         }
#     ]
# ).choices[0].message.content



# print(prompt)

# prompt = """classify below email into one of the categories
# 1. Billing issue
# 2. Technical issue
# 3. General inquiry
# email : {1}
# subject : {0}
# """.format(email_body,email_subject)

# print(prompt)
