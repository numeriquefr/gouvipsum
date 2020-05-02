import random


with open("words.txt") as f:
    words = set([l.strip() for l in f.readlines()])

for _ in range(50):
    nb = random.randint(3, 5)
    print(" ".join(random.sample(words, nb)))
