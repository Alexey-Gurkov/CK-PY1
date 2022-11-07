import random

def get_random_password() -> str:
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    all_symbol = ascii_uppercase + ascii_lowercase + digits
    long = random.randint(8, 16)
    password = "".join(random.sample(all_symbol, long))
    return password


print(get_random_password())
