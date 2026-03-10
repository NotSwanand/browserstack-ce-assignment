import string
from collections import Counter


def find_repeated_words(translated_titles):

    words = []

    for title in translated_titles:

        clean = title.lower().translate(
            str.maketrans('', '', string.punctuation)
        )

        words.extend(clean.split())

    counts = Counter(words)

    found = False

    for word, count in counts.items():
        if count > 2:
            print(word, count)
            found = True

    if not found:
        print("No repeated words found")