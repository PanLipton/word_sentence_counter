import pytest
from word_sentence_counter import word_count, sentence_count, count_words_sentences

@pytest.fixture
def example_text():
    return "This is a sample text. It contains 3 sentences! Can you count them?"

def test_word_count(example_text):
    assert word_count(example_text) == 13

def test_sentence_count(example_text):
    assert sentence_count(example_text) == 3

@pytest.mark.parametrize("file_content, expected_words, expected_sentences", [
    ("Hello world! This is a test.", 6, 2),
    ("Another example. With multiple sentences. And some more words!", 9, 3),
])
def test_count_words_sentences(tmp_path, file_content, expected_words, expected_sentences):
    file_path = tmp_path / "test.txt"
    file_path.write_text(file_content)
    words, sentences = count_words_sentences(file_path)
    assert words == expected_words
    assert sentences == expected_sentences