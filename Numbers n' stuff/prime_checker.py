from math import sqrt

def isPrime(n):
    if n == 2 or n == 3: return True
    if n <2 or n % 2 == 0 or n % 3 == 0: return False
    #If n is divisble by 2 and 3 then it can't be prime
    for num in range(5, int(sqrt(n)+1),2):
    #Check whether n is divisible by 5 or its squareroot
        if n % num == 0:
            return False
    return True

def Primesfrom1to100():
    print(*[i for i in range(100) if isPrime(i)])

def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

z = 7
print(is_prime(z))
