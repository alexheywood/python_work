#This function returns the intersect of the two arrays provided.
#Time complexity: O(n)

def intersect(array1, array2):

    hashTable = {}
    intersectArray = []

    
    if len(array1) >= len(array2):
        bigArray = array1
        smallArray = array2
        
    else:
        bigArray = array2
        smallArray = array1

    for item in bigArray:
        hashTable[item] = True

    for item in smallArray:
        if hashTable.get(item):
            intersectArray.append(item)

    return intersectArray
        

 
