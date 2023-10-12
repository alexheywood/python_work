#This function returns a character if it is present twice in the provided array.

def intersect(array):

    hashTable = {}

    for item in array:
        if hashTable.get(item):
            return item

        else:
            hashTable[item] = True

    return False


print(intersect(['a','c','c','e','d']))
