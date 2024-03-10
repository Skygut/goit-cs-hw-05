import requests
from collections import Counter
import re
import matplotlib.pyplot as plt
from functools import reduce
from collections import defaultdict


def map_function(text):
    words = text.split()
    return [(word, 1) for word in words]


def shuffle_function(mapped_values):
    shuffled = defaultdict(list)
    for key, value in mapped_values:
        shuffled[key].append(value)
    return shuffled.items()


def reduce_function(shuffled_values):
    reduced = {}
    for key, values in shuffled_values:
        reduced[key] = sum(values)
    return reduced


# Виконання MapReduce
def map_reduce(text):
    # Крок 1: Мапінг
    mapped_values = map_function(text)

    # Крок 2: Shuffle
    shuffled_values = shuffle_function(mapped_values)

    # Крок 3: Редукція
    reduced_values = reduce_function(shuffled_values)

    return reduced_values


if __name__ == "__main__":
    #   Вхідний текст для обробки
    text = "hello world hello Python hello Student"

    # Виконання MapReduce на вхідному тексті
    result = map_reduce(text)

    print("Результат підрахунку слів:", result)


# def fetch_text(url):
#     response = requests.get(url)
#     return response.text


# def main(url):
#     text = fetch_text(url)
#     # word_counts = map_reduce(text)
#     # visualize_top_words(word_counts)
#     result = map_reduce(text)

#     print("Результат підрахунку слів:", result)


# if __name__ == "__main__":
#     url = "https://www.gutenberg.org/files/11/11-0.txt"  # Alice in Wonderland by Lewis Carroll
#     main(url)
