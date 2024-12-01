def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_tough_prime(number):

    while number > 0:
        if not is_prime(number):
            return False
        number //= 10 
    return True

def generate_tough_primes(n, current=""):
    if len(current) == n:
        print(current)
        return
    

    for digit in "23579" if current == "" else "0123456789":
        new_number = current + digit
        if is_prime(int(new_number)):
            generate_tough_primes(n, new_number)


n = int(input())
generate_tough_primes(n)
