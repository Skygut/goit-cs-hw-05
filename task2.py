import requests
from collections import Counter
import re
import matplotlib.pyplot as plt
from functools import reduce
from collections import defaultdict


def map_reduce(text):
    words = text.split()
    mapped_values = [(word, 1) for word in words]

    shuffled = defaultdict(list)
    for key, value in mapped_values:
        shuffled[key].append(value)

    reduced = {key: sum(values) for key, values in shuffled.items()}

    return reduced


def visualize_top_words(word_counts, top_n=20):
    top_words = dict(Counter(word_counts).most_common(top_n))
    print(top_words)
    plt.bar(top_words.keys(), top_words.values())
    plt.xlabel("Слова")
    plt.ylabel("Частота")
    plt.title("Топ-слова за частотою використання")
    plt.xticks(rotation=45)
    plt.show()


def fetch_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")


def main(url):
    text = fetch_text(url)
    word_counts = map_reduce(text)
    visualize_top_words(word_counts)


if __name__ == "__main__":
    url = "https://www.gutenberg.org/files/11/11-0.txt"  # Alice in Wonderland by Lewis Carroll
    main(url)
