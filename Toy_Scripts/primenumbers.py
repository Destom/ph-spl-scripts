def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x > 2:
        for n in range(2, x-1):
            if x % n == 0:
               return False
        else:
            return True
