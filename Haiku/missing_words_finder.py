import sys
from string import punctuation
import pprint
import json
from nltk.corpus import cmudict

cmudict = cmudict.dict()


def main():
    haiku = load_haiku('train.txt')
    exceptions = cmudict_missing(haiku)
    build_dict = input("\nBuild an exception dictionary manually (y/n)? \n")
    if build_dict.lower() == "n":
        sys.exit()
    else:
        missing_words_dict = make_exceptions_dict(exceptions)
        save_exceptions(missing_words_dict)


def load_haiku(filename):
    """Open and return traning part haiku as a set."""
    with open(filename) as in_file:
        haiku = set(in_file.read().replace('-', ' ').split())
        return haiku


def cmudict_missing(word_set):
    """Find and return words in a set of words that are
       missing in cmudict"""
    exceptions = set()
    for word in word_set:
        word = word.lower().strip(punctuation)
        if word.endswith("'s") or word.endswith("`s"):
            word = word[:-2]
        if word not in cmudict:
            exceptions.add(word)


        print("\nExceptions")
        print(*exceptions, sep='\n')
        print("\nNumber of unique words in the haiku corpus = {}".format(len(word_set)))
        print("The number of words in the non-cmudict word corpus = {}".format(len(exceptions)))
        membership = (1 - (len(exceptions) / len(word_set))) * 100
        print("Membership in cmudict = {:.1f}{}".format(membership, '%'))
        return exceptions


def make_exceptions_dict(exceptions_set):
    """Return the dictionary of words and the number of syllables from the set of words."""
    missing_words = {}
    print("Enter the number of syllables. Errors can be corrected at the end. \n")
    for word in exceptions_set:
        while True:
            num_sylls = input("Enter the number of syllables {}: ".format(word))
            if num_sylls.isdigit():
                break
            else:
                print("         An invalid response", file=sys.stderr)
        missing_words[word] = int(num_sylls)
    print()
    pprint.pprint(missing_words, width = 1)
    print("\nMake changes to the dictionary before saving?")
    print("""
    0 - Save and close
    1 - Add word or change syllables num
    2 - Remove word
    """)

    while True:
        choice = input("\nMake your choice: ")

        if choice == 0:
            break
        elif choice == '1':
            word = input("\nAdded or modified word: ")
            missing_words[word] = int(input("Enter the num of syllables {}: ".format(word)))

        elif choice == '2':
            word = input("\nEnter the word to delete: ")
            missing_words.pop(word, None)

        print("\nChanges in new words and syllables:")
        pprint.pprint(missing_words, width=1)

        return missing_words


def save_exceptions(missing_words):
    """Save exceptions dictionary as a json file"""
    json_string = json.dumps(missing_words)
    f = open('missing_words.json', 'w')
    f.write(json_string)
    f.close()
    print("\nFile saved as missing_words.json")


if __name__ == "__main__":
    main()

