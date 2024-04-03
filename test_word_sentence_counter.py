import pytest
from word_sentence_counter import word_count, sentence_count, count_words_sentences

@pytest.fixture
def example_text():
    return "This is a sample text. It contains 3 sentences! Can you count them?"

def test_word_count(example_text):
    assert word_count(example_text) == 14

def test_sentence_count(example_text):
    assert sentence_count(example_text) == 3
