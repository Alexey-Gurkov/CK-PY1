import random
import string


def get_random_password(long_) -> str:
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits_ = string.digits
    all_symbol = lowercase + uppercase + digits_
    password = "".join(random.sample(all_symbol, long_))
    return password


size_start_password, size_stop_password = 8, 16
long_password = random.randint(size_start_password, size_stop_password)
print(get_random_password(long_password))
