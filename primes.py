"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import math
def primes(number_of_primes):
    list = [2]
    divided = False
    counter = 3
    primes_found = 1
    while primes_found < number_of_primes:
        for y in range(int(math.sqrt(counter)), counter):
            if counter % y == 0 and y != 1 and counter != y:
                divided = True
                break
        if not divided:
            list.append(counter)
            primes_found += 1
        divided = False
        counter += 1
    return list


print(primes(20))
print(len(primes(20)))