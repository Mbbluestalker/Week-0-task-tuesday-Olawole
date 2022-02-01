def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def print_factors(x):
    arr = []
    for i in range(1, x + 1):
        if x % i == 0:
            arr.append(i)
    return arr

def check_prime(n):
    if is_prime(n) == True:
        return f"{n} is  a prime number"
    else:
        mul_not_prime = print_factors(n)
        return f"{n} is not a prime number,\n {mul_not_prime}"

print(check_prime(34))