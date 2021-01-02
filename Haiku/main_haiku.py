import sys 
import logging
import random
from collections import defaultdict
from count_syllables import count_syllables


logging.disable(logging.CRITICAL)

logging.basicConfig(level=logging.DEBUG, format="%(message)s")


def load_training_file(file):
    """Return a text file as a character string"""
    with open(file) as f:
        raw_haiku = f.read()
        return raw_haiku


def prep_training(raw_haiku):
    """Load character string, remove newline characters, split into words by spaces, and return the list """
    corpus = raw_haiku.replace('\n', '').split()
    return corpus


def map_word_to_word(corpus):
    """Download the list and apply the dictionary to link the word to
       the next word"""
    limit = len(corpus) - 1
    dict1_to_1 = defaultdict(list)
    for index, word in enumerate(corpus):
        if index < limit:
            suffix = corpus[index + 1]
            dict1_to_1[word].append(suffix)
    logging.debug("result \"sake\"= %s\n", dict1_to_1['sake'])
    return dict1_to_1


def map_2_words_to_word(corpus):
    """Download the list and use the dictionary to link the
       dictionary pair to the closing word"""
    limit = len(corpus) - 2
    dict2_to_1 = defaultdict(list)
    for index, word in enumerate(corpus):
        if index < limit:
            key = word + ' ' + corpus[index + 1]
            suffix = corpus[index + 2]
            dict2_to_1[key].append(suffix)

    logging.debug("results of linking 2 words to a phrase \"sake jug\" = %s\n", dict2_to_1['sake jug'])
    return dict2_to_1


def random_word(corpus):
    """Return random word"""
    word = random.choice(corpus)
    num_syls = count_syllables(word)
    if num_syls > 4:
        random_word(corpus)
    else:
        logging.debug("random word and syls = %s %s\n", word, num_syls)

        return (word, num_syls)


def word_after_single(prefix, suffix_map_1, current_syls, target_syls):
    pass


def word_after_double(prefix, suffix_map_2, current_syls, target_syls):
    pass


def haiku_line(suffix_map_1, suffix_map_2, corpus, end_prev_line, target_syls):
    pass


def main():
    pass