import random as rand

def lots_of_random_numbers(n):
    sum = 0
    for i in range(n):
        sum += rand.randint(1, 6)
    return sum

print(lots_of_random_numbers(500000000))