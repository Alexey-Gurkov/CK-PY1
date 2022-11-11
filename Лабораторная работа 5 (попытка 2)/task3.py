import random


def get_unique_list_numbers(start=-10, stop=10, size=15) -> list[int]:

    random_list = []
    while len(random_list) != size:
        number = random.randint(start, stop)
        if number not in random_list:
            random_list.append(number)

    return random_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
