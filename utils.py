def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
<<<<<<< HEAD
<<<<<<< Updated upstream
    return True
=======
    return True

def five(num):
    while num > 1:
        if num % 5 != 0:
            return False
        num /= 5
    return num == 1

def two(number):
    while number > 1:
        if number % 2 != 0:
            return False
        number //= 2
    return number == 1
>>>>>>> Stashed changes
=======
    return True

def five(num):
    return num & (num - 1) == 0 and num != 0
>>>>>>> dev5
