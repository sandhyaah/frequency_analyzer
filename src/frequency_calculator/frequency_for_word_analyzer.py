from src.i_word_frequency_analyzer import IWordFrequencyAnalyzer


def calculate_frequency_for_word(user_input, word):
    most_frequent = dict(IWordFrequencyAnalyzer(user_input).calculate_most_frequent_word())
    if word in most_frequent:
        return most_frequent.get(word)
