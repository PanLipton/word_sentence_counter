import pytest
from word_sentence_counter import word_count, sentence_count, count_words_sentences

@pytest.fixture
def example_text():
    return "This is a sample text. It contains 3 sentences! Can you count them?"