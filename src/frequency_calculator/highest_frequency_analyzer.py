from src.i_word_frequency_analyzer import IWordFrequencyAnalyzer


def calculate_highest_frequency(user_input):
    most_frequent = IWordFrequencyAnalyzer(user_input).calculate_most_frequent_word()
    highest_frequency = []
    for i in range(len(most_frequent)):
        if most_frequent[i][1] == most_frequent[0][1]:
            highest_frequency.append(most_frequent[i])
    return highest_frequency
