"""
Concept: Find Next Prime

This example demonstrates mathematical algorithms, efficiency, and control flow.
Students will learn about prime numbers, optimization techniques, and function design.
"""

# Task 5 - Find Next Prime (Example File)
# This file demonstrates prime number algorithms and optimization


def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def next_prime(n):
    """Find the next prime number after n"""
    p = n + 1
    while not is_prime(p):
        p += 1
    return p


# Test the functions
print("Testing prime functions:")
print(f"is_prime(17): {is_prime(17)}")
print(f"is_prime(18): {is_prime(18)}")
print(f"next_prime(17): {next_prime(17)}")
print(f"next_prime(18): {next_prime(18)}")

# Find multiple next primes (Uncomment Below)
# -------------------------------------------
# print("\nFinding next primes:")
# for num in [10, 20, 30, 40, 50]:
#     next_p = next_prime(num)
#     print(f"Next prime after {num}: {next_p}")

# Generate a list of primes (Uncomment Below)
# -------------------------------------------
# def generate_primes(count):
#     """Generate the first 'count' prime numbers"""
#     primes = []
#     num = 2
#     while len(primes) < count:
#         if is_prime(num):
#             primes.append(num)
#         num += 1
#     return primes
#
# first_10_primes = generate_primes(10)
# print(f"\nFirst 10 primes: {first_10_primes}")

# Optimized prime checking (Uncomment Below)
# -------------------------------------------
# def is_prime_optimized(n):
#     """Optimized prime checking with early returns"""
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#
#     # Only check odd divisors up to sqrt(n)
#     for i in range(3, int(n ** 0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True
#
# # Test optimized version
# print("\nTesting optimized prime function:")
# for num in [2, 3, 4, 5, 17, 18, 97, 100]:
#     result = is_prime_optimized(num)
#     print(f"is_prime_optimized({num}): {result}")

# Prime factorization (Uncomment Below)
# -------------------------------------------
# def prime_factors(n):
#     """Find all prime factors of a number"""
#     factors = []
#     d = 2
#     while d * d <= n:
#         while n % d == 0:
#             factors.append(d)
#             n //= d
#         d += 1
#     if n > 1:
#         factors.append(n)
#     return factors
#
# print("\nPrime factorization examples:")
# for num in [12, 28, 60, 97]:
#     factors = prime_factors(num)
#     print(f"Prime factors of {num}: {factors}")

# Performance comparison (Uncomment Below)
# -------------------------------------------
# import time
#
# def time_function(func, *args):
#     """Time how long a function takes to execute"""
#     start_time = time.time()
#     result = func(*args)
#     end_time = time.time()
#     return result, end_time - start_time
#
# # Compare performance
# test_number = 1000003
#
# result1, time1 = time_function(is_prime, test_number)
# result2, time2 = time_function(is_prime_optimized, test_number)
#
# print(f"\nPerformance comparison for {test_number}:")
# print(f"Basic is_prime: {result1} (took {time1:.6f} seconds)")
# print(f"Optimized is_prime: {result2} (took {time2:.6f} seconds)")
# print(f"Speed improvement: {time1/time2:.2f}x faster")
