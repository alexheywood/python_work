def checkPassword(password: str) -> bool:
    has_letter = False
    has_digit = False
    for character in password:
        if '0' <= character <= '9':
            has_digit = True
        if 'a' <= character <= 'z':
            has_letter = True
        if has_letter and has_digit:
            return True
        
    return False
