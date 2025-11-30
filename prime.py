# def is_prime(num):
#     if num <= 1:
#         return False
#     if num <= 3:
#         return True
#     if num%2 == 0 or num%3 == 0:
#         return False
    
#     i = 5
#     while i*i <= num:
#         if n%i == 0 or n%(i+2) == 0:
#             return False
#         i = i+6
#     return True

# number = 7
# print(is_prime(number))

# 

def isprime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

print(isprime(16))