import re

def word_count(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)

