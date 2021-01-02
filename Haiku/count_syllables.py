import sys
from string import punctuation
import json
from nltk.corpus import cmudict


# Load dict from haiku corpus
with open('missing_words.json') as f:
    missing_words = json.load(f)

cmudict = cmudict.dict()


def count_syllables(words):
    """Use a corpus for count syllables"""
    words = words.replace('-', ' ')
    words = words.lower().split()
    num_sylls = 0

    for word in words:
        word = word.strip(punctuation)
        if word.endswith("'s") or word.endswith("`s"):
            word = word[:-2]
        if word in missing_words:
            num_sylls += missing_words[word]
        else:
            for phonemes in cmudict[word][0]:
                for phoneme in phonemes:
                    if phoneme[-1].isdigit():
                        num_sylls += 1
    return num_sylls


def main():
    while True:
        print("Logs counter")
        word = input("Enter the word or phrase or press enter for exit")

        if word == '':
            sys.exit()
        try:
            num_syllables = count_syllables(word)
            print("Number of syllables in {} = {}".format(word, num_syllables))
            print()
        except KeyError:
            print("Word not found. Try again\n", file=sys.stderr)


if __name__ == "__main__":
    main()
