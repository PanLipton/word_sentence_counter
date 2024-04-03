import re

def word_count(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def sentence_count(text):
    sentences = re.split(r'[.!?]+', text)
    return len([s for s in sentences if s.strip()])

