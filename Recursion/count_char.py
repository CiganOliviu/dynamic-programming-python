
def count_char(string, char):

    if len(string) <= 0:
        return 0

    if string[0] == char:
        return 1 + count_char(string[1:], char)
    else:
        return count_char(string[1:], char)


assert(count_char("Jerry", "r") == 2)
assert(count_char("Audi A4", "A") == 2)
assert(count_char("The best", "e") == 2)
assert(count_char("A4", "6") == 0)
