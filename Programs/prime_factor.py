# Find the prime factors of given number  


def get_prime_factors(n):
    factors = list()
    divisor = 2
    while (divisor <= n):
        if (n % divisor) == 0:
            factors.append(divisor)
            n = n / divisor
        else:
            divisor += 1
    print(factors)


user = int(input())
get_prime_factors(n=user)


