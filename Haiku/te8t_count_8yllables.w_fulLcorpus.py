import sys
import count_syllables

with open('train.txt') as in_file:
    words = set(in_file.read().split())

missing = []

for word in words:
    try:
        num_syllables = count_syllables.count_syllables(word)
    except KeyError:
        missing.append(word)

print("Missing words: ", missing, file=sys.stderr)