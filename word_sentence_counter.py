import re

def word_count(text):
    words = re.findall(r"\b[\w-']+\b", text)
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
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Використання: python word_sentence_counter.py <шлях_до_файлу>")
    else:
        file_path = sys.argv[1]
        words, sentences = count_words_sentences(file_path)
        print(f'У тексті {words} слів і {sentences} речень')