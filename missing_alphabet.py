#This function returns the character that is missing from the alphabet.

def missing_char(word):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    hashWord = {}

    for x in word:
        hashWord[x] = True

    for x in alphabet:
        if not(hashWord.get(x)):
            return x
