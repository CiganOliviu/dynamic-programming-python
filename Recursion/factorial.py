def get_factorial_number(number):

    if number == 0:
        return 1

    return number * get_factorial_number(number - 1)

assert(get_factorial_number(0) == 1)
assert(get_factorial_number(1) == 1)
assert(get_factorial_number(7) == 5040)
assert(get_factorial_number(8) == 40320)
assert(get_factorial_number(4) == 24)
