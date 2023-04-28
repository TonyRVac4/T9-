"""
Функция t9, принимает на вход строку, состоящую из цифр 2–9,
и возвращает список слов английского языка, которые можно получить из этой последовательности цифр.
"""

from typing import List, Dict


PHONE_KEYS: Dict[str, tuple] = {
    "2": ("a", "b", "c"),
    "3": ("d", "e", "f"),
    "4": ("g", "h", "i"),
    "5": ("j", "k", "l"),
    "6": ("m", "n", "o"),
    "7": ("p", "q", "r", "s"),
    "8": ("t", "u", "v"),
    "9": ("w", "x", "y", "z")
}


with open("/usr/share/dict/words", "r") as words_file:
    words_list: list = [word.lower().replace("\n", "") for word in words_file.readlines()]


def my_t9(input_numbers: str) -> List[str]:
    filtered_words_by_len = tuple(filter(lambda word: len(word) == len(input_numbers), words_list))

    prev_words: tuple = filtered_words_by_len

    for letter_index, num in enumerate(input_numbers):
        possible_tellers: tuple = PHONE_KEYS[num]
        filtered_words_by_letter: tuple = tuple(filter(lambda word: word[letter_index] in possible_tellers, prev_words))
        prev_words: tuple = filtered_words_by_letter

    return list(prev_words)


if __name__ == '__main__':
    numbers: str = "22736368"
    words: List[str] = my_t9(numbers)
    print(*words, sep='\n')
