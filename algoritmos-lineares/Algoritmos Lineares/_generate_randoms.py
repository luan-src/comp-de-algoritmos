import random

def generate_randoms(max):
    random_numbers = []
    for i in range(1, max+1):
        random_numbers.append(random.randint(1, 1000))
    return random_numbers