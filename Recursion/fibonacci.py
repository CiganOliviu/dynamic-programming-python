def get_fibonacci_number(number):

    if number == 1 or number == 2:
        return 1

    return get_fibonacci_number(number - 1) + get_fibonacci_number(number - 2)


assert(get_fibonacci_number(1) == 1)
assert(get_fibonacci_number(8) == 21)
assert(get_fibonacci_number(12) == 144)
assert(get_fibonacci_number(15) == 610)
