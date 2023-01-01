import random

def flip_coin():
    choices = ["heads", "tails"]
    coin_flip = print(random.choice(choices))
    return coin_flip

flip_coin()
