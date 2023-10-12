"""
This python Flashcard program shows a random vehicle to the user.
If the user types 'q' it will not show the definition. otherwise
The definition is returned to the user. The user can re-enter a value or
enter 'quit' to exit the program.
"""
from random import *

glossary = {'bike': 'A two wheeled vehicle.',
            'car' : 'A four wheeled vehicle.',
            'plane' : 'A flying vehicle.',
            'boat' : 'A vehicle that floats on water.'}

exit = False;

def flashcard():
    random = choice(list(glossary))
    print('The definition of:', random)
    print(glossary[random])


while exit is not True:
    
    user_input = input('Enter s to check glossary or q to quit: ')

    if user_input == 'q':
        exit = True;

    elif user_input == 's':
        flashcard()

    else:
        print('You need to type either \'y\' or \'q\'')
        
        
