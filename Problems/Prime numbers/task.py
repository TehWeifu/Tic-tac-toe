prime_numbers = []
divisors = []

prime_numbers.append(2)

for n in range(3, 1001):
    for div in range(2, n):
        divisors.append(n % div)

    if all(divisors):
        prime_numbers.append(n)

    divisors = []
