#This function uses recursion to count how many characters are in a list

array = ["a", "bg", "cko", "lops"]

def functional_count(chars, count=0):
    total = count
    for item in chars:
        for x in item:
            count = count + 1

    return count


def recursive_count(array):
    if len(array) == 0:
        return 0

    return len(array[0]) + recursive_count(array[1:])
