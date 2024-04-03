import re

def word_count(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def sentence_count(text):
    sentences = re.split(r'[.!?]+', text)
    return len([s for s in sentences if s.strip()])

def count_words_sentences(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = word_count(text)
        sentences = sentence_count(text)
        return words, sentences