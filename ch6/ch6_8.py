def is_prime(num):
    if num <= 1:
        return False
    if num == 2:  
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes_less_than(n):
    prime_numbers = []
    for i in range(2, n):
        if is_prime(i):
            prime_numbers.append(i)
    return prime_numbers


n = int(input("enter number int : "))
print("this is lit number ", primes_less_than(n))