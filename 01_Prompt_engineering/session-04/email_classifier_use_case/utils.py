from business_logic import classify_with_cot, classify_with_self_consistency,draft_response_with_tot

enterprise_customers = ["enterprise1@rbyteai.com", "enterprise2@bigcompany.com"]

def is_enterprise_customer(sender):
    if sender in enterprise_customers:
        return True
    return False

def process_email(email):
    # step 1 : Classify the email using COT
    intial = classify_with_cot(email['subject'], email['body'], email['sender'])
    # Step 2 : check for high stakes customers
    is_enterprise = is_enterprise_customer(email['sender'])
    if is_enterprise:
        # Handle enterprise customer case
        final = classify_with_self_consistency(email)
    else:
        final = intial

    routing = {
        "Billing"        : "billing-team@company.com",
        "Technical"      : "tech-support@company.com",
        "Feature Request": "product@company.com",
        "Spam"           : None,
    }

    routed_to = routing.get(final['category'],"support@company.com")

    is_churn_risk = (
        "cancel" in email['body'].lower()
        or "not satisfied" in email['body'].lower()
        or "bad experience" in email['body'].lower()
    ) 

    drafted_response = None
    if is_churn_risk:
        drafted_response = draft_response_with_tot(email, final)

    return {
        "email_id"          : email.get("id", "N/A"),
        "classification"    : final,
        "routed_to"         : routed_to,
        "drafted_response"  : drafted_response,
        "needs_human_review": final.get("needs_human_review", False),
        "audit_trail"       : final.get("reasoning_traces", [])
    }


# test it
email = {
    "id": 8,
    "subject": "App Freezing",
    "sender": "user@client.com",
    "body": "The app keeps freezing when I try to open it. I am planning to cancel my subscription.",
    "correct_label": "Technical",
    "urgency": "High",
    "difficulty": "easy",
    "why_tricky": "The description of the app freezing is a clear technical issue."
  }

import json
with open("test_emails.json", "r") as f:
    email = json.load(f)

for i in email[:3]:
    output = process_email(i)
    print(output)
