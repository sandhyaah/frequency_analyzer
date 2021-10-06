from src.i_word_frequency_analyzer import IWordFrequencyAnalyzer


def calculate_most_frequent_N_words(user_input, number):
    user_input.sort()
    most_frequent = IWordFrequencyAnalyzer(user_input).calculate_most_frequent_word()
    return most_frequent[:number]
