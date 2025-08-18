import random

def generate_random_numbers(count):
    numbers = []
    for _ in range(count):
        numbers.append(random.randint(1, 100))
    return numbers

random_numbers = generate_random_numbers(10)

print("10 números random del 1 al 100 (sin ordenar):", random_numbers)

print("10 números random del 1 al 100 (ordenados):", sorted(random_numbers))
