import re
from src.frequency_calculator.highest_frequency_analyzer import calculate_highest_frequency
from src.frequency_calculator.frequency_for_word_analyzer import calculate_frequency_for_word
from src.frequency_calculator.most_frequent_N_words_analyzer import calculate_most_frequent_N_words


if __name__ == '__main__':
    user_entry = input('Enter any string: ').lower()
    word = input('Enter a word to calculate frequency: ').lower()
    number = int(input('Enter a number to calculate the frequency of N words: '))
    user_entry = re.sub('''[0-9><""!,*=\\\+@'#;:/%&'$_?.^-]''', '', user_entry)
    user_entry = re.sub('[\([{})\]]', '', user_entry)
    user_input = user_entry.split()
    task1 = calculate_highest_frequency(user_input)
    task2 = calculate_frequency_for_word(user_input, word)
    task3 = str((calculate_most_frequent_N_words(user_input, number)))[1:-1]
    print('Highest frequency word: ', task1)
    print(f'''Frequency for "{word}": ''', task2)
    print(f'Most frequent {number} word: {{{task3}}}')
