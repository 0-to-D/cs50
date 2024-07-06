import random
from random import choice as ch
from random import randint as rint

print(ch(["heads", "tales"]))

print(rint(0,9284))

listt = ["jack", "king", "queen"]

random.shuffle(listt)

for card in listt:
    print(card)

