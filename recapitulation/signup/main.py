from alphabet_detector import AlphabetDetector
import re

def signUp(username, email, password):
    
    if type(username) != str or type(email) != str or type(password) != str:
        raise TypeError("incorect type of variable(s)")

    if len(username) < 5 and len(username) > 12:
        raise TypeError("username must be at least 5 and at most 12 characters long")

    ad = AlphabetDetector()

    for i in range(len(username)):
        if ad.only_alphabet_chars(username[i], "LATIN") == False and username[i].isdigit() == False:
            raise Exception("username must consists only of latin (a..zA..Z) letters and digits (0..9)")
    
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if re.fullmatch(pattern, email) == False:
        raise Exception("email is not valid")

    if len(password) < 8:
        raise TypeError("password must be at least 8 characters long")

    result = dict([
        ('username', username),
        ('email', email),
        ('password', password)
    ])

    return result

print(signUp('John', 'John@gmail.com', '21_John_21'))