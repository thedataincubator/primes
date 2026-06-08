import math

def is_prime(n):
    """This checks whether a number is prime or not
    5 should return True
    6 should return False

    :n: n

    output is a bool
    """

    if not isinstance(n, int):
        raise RuntimeError("Can only test integers")

    # special cases
    if n == 1:
        return False
    if n == 2:
        return True

    sqrtn = int(math.sqrt(n))

    # we want to go all the way to sqrtn
    # so the range needs to go to sqrtn + 1 (exclusive behavior in Python)
    for number in range(2, sqrtn + 1):
        if n % number == 0:
            return False

    return True

