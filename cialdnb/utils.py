import random
import re

# Get user agents from a pre-set list
with open("user_agent_list.txt", "r") as f:
    user_agent_list = []
    for line in f:
        if not line.startswith("#"):
            user_agent_list.append(line)


def find_phone_number(html_text):
    return re.findall(r"\+?\d{2}\s?0?\d{10}", html_text)


def phone_cleanup(phone_list):
    """Perform a light clean up on phone numbers"""
    clean_phones = []
    for phone in phone_list:
        clean = re.sub(r"[^0-9\(\)+]", " ", phone)
        clean_phones.append(clean)
    return list(set(clean_phones))


def random_agent():
    """Get a random user agent from a pre determined user agent list"""
    return random.choice(user_agent_list)
