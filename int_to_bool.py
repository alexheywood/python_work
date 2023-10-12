def truth_value(integer1,integer2):
    integer3 = 0
    """Convert an integer into a truth value."""
    # Convert 0 into False and all other integers,
    # including 1, into True
    if integer1 == 0 and integer2 == 0:
        integer3 == 0
    elif integer1 == 0 and integer2 ==1:
        integer3 = 0
    elif integer1 == 1 and integer2 == 0:
        integer3 = 0
    elif integer1 == 1 and integer2 == 1:
        integer3 = 1
        
    print(integer3)
