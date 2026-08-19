import re
from typing import Optional

def extract_email_regex(text: str) -> Optional[str]:
    email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    email = re.findall(email_regex, text)
    if email:
        return email[0]
    return None

# print(extract_email_regex("My email is example@rbyteai.com"))
def extract_email(text: str) -> Optional[str]:
    email = extract_email_regex(text)
    if email:
        return email
    return None


def build_candidate_id (text,file_name):
    email = extract_email(text)
    if email:
        return email
    import hashlib # think on this ? 
    fallback_id = hashlib.md5((file_name).encode()).hexdigest()[:16]
    return fallback_id

# print(build_candidate_id("My email is ", "test_files.txt"))