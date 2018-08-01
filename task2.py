import random
import array
reversePhrase = list()

words = [word.rstrip('\n') for word in open('words.txt')]
randomPhrase = " ".join([words[random.randrange(0, len(words))] for i in range(4)])

reversePhrase = randomPhrase[::-1]

print(randomPhrase)
print(reversePhrase)