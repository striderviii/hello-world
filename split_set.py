
# Splits a set of numbers in half
# If both sets are even, returns two sets in half
# If not, adds a underdash to second set

def split_set(a):
    # Turns numbers into a list
    list_a = [x for x in (a)]
    # Checks if list is even amount
    if len(list_a) % 2 == 0:
        # Splits into two sets in half of value of length
        list_a = [a[:len(a)//2]] + [a[len(a)//2:]]
        return list_a
    else:
        # Does same but adds a underscore to second set
        list_1 = [a[:len(a)//2+1]]
        list_2 = [a[len(a)//2+1:] + "_"]

        return list_1 + list_2

print(split_set("abcdew"))
