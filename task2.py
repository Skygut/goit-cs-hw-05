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
    mapped_values = map_function(text)
    shuffled_values = shuffle_function(mapped_values)
    reduced_values = reduce_function(shuffled_values)
    return reduced_values


# def map_reduce1(text):
#     words = re.findall(r"\w+", text.lower())
#     mapped_words = map(lambda word: (word, 1), words)
#     sorted_words = sorted(mapped_words)
#     reduced_words = reduce(
#         lambda acc, val: acc.update({val[0]: acc.get(val[0], 0) + 1}) or acc,
#         sorted_words,
#         {},
#     )
#     print(reduced_words)
#     return reduced_words


def visualize_top_words(word_counts, top_n=10):
    top_words = dict(Counter(word_counts).most_common(top_n))
    plt.bar(top_words.keys(), top_words.values())
    plt.xlabel("Слова")
    plt.ylabel("Частота")
    plt.title("Топ-слова за частотою використання")
    plt.xticks(rotation=45)
    plt.show()


def fetch_text(url):
    response = requests.get(url)
    return response.text


def main(url):
    text = fetch_text(url)
    word_counts = map_reduce(text)
    visualize_top_words(word_counts)


if __name__ == "__main__":
    url = "https://www.gutenberg.org/files/11/11-0.txt"  # Alice in Wonderland by Lewis Carroll
    main(url)
