import json
from unittest import result
from dotenv import load_dotenv
from openai import OpenAI
import os
import time
from collections import Counter
load_dotenv()
print(load_dotenv())
client = OpenAI()



def call_llm(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content

# print(call_llm("Hello, how are you?"))


def load_prompt(filename):
    path = os.path.join('prompt', filename)
    with open(path, 'r') as file:
        return file.read()
    
# test it
def classify_with_cot(subject,body,sender):
    template = load_prompt("classify_cot.md")
    prompt = template.format(subject=subject, body=body, sender=sender)
    result = call_llm(prompt)
    category, urgency = None,None
    for line in result.split("\n"):
        if "CATEGORY:" in line:
            category = line.split(":", 1)[1].strip()
        elif "URGENCY:" in line:
            urgency = line.split(":", 1)[1].strip()

    return {
        "category": category,
        "urgency": urgency,
        "full_output": result
    }


def classify_with_self_consistency(email, n_runs = 1):
    template = load_prompt("classify_cot.md")
    results = []
    traces = []
    for i in range(n_runs):
        prompt = template.format(subject=email['subject'], body=email['body'], sender=email['sender'])
        result = call_llm(prompt)
        traces.append(result)
        for line in result.split("\n"):
            if "CATEGORY:" in line:
                category = line.split(":", 1)[1].strip()
                results.append(category)
    
    votes = Counter(results)
    winner = votes.most_common(1)[0]
    print(type(winner))

    print(winner)
    confidence = winner[1] / n_runs*100
    urgency = None
    for line in traces[0].split("\n"):
        if "URGENCY:" in line:
            urgency = line.split(":", 1)[1].strip()

    final_output = {
        "category": winner[0],
        "confidence": confidence,
        "urgency": urgency
    }

    return final_output


# "THINKING:
# 1. Surface complaint: The app keeps freezing when I try to open it.
# 2. Root cause: This likely indicates a technical issue related to the app's performance or software stability.
# 3. Team that OWNS this: Technical team.
# 4. Business impact: If the app is freezing, it may prevent users from utilizing the service, which can lead to dissatisfaction and potential loss of business.

# CATEGORY: Technical
# URGENCY: High"

email = {
    "id": 8,
    "subject": "App Freezing",
    "sender": "user@client.com",
    "body": "The app keeps freezing when I try to open it.",
    "correct_label": "Technical",
    "urgency": "High",
    "difficulty": "easy",
    "why_tricky": "The description of the app freezing is a clear technical issue."
  }
# output =classify_with_self_consistency(email)
# print(output)

{'category': 'Technical', 'confidence': 100.0, 'urgency': 'High'}

# {'category': 'Technical', 'urgency': 'High', 'full_output': "THINKING:\n1. Surface complaint: The app keeps freezing when trying to open it.\n2. Root cause: There may be a technical issue with the app's code, compatibility with the device, or server response problems.\n3. Team that OWNS this: Technical Support Team.\n4. Business impact: If the app is freezing, it could prevent users from accessing important features, leading to a potential loss of productivity and frustration for customers.\n\nCATEGORY: Technical\nURGENCY: High"}


def draft_response_with_tot(email, classification):
    template = load_prompt("tree_of_thought.md")
    prompt   = template.format(
        subject =email["subject"],
        body    =email["body"],
        category=classification["category"]
    )
    return call_llm(prompt)