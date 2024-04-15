import matplotlib.pyplot as plt

def middle_square(seed, digits):
    # Function to generate a random number using the middle square method
    result = seed
    for _ in range(digits):
        result = int(str(result * result).zfill(2 * digits)[digits//2: -digits//2])
        yield result

# Example usage:
seed = 1234  # Initial seed
digits = 4   # Number of digits in the generated random number
iterations = 5  # Number of random numbers to generate

print(f"Random numbers using middle square method with seed {seed}:")
for i, number in enumerate(middle_square(seed, digits), start=1):
    print(f"Random number {i}: {number}")
    if i == iterations:
        break




def linear_congruence(seed, a, c, m, n):
    # Function to generate a random number using linear congruence method
    result = seed
    for _ in range(n):
        seed = (a * result + c) % m
        yield result

# Example usage:
seed = 7  # Initial seed
a = 1664525  # Multiplier
c = 113604223  # Increment
m = 2**32  # Modulus
n = 100000  # Number of random numbers to generate

print(f"Random numbers using linear congruence method with seed {seed}:")
for i, number in enumerate(linear_congruence(seed, a, c, m, n), start=1):
    print(f"Random number {i}: {number}")