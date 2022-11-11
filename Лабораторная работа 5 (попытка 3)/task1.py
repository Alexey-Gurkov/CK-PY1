from pprint import pprint

numbers_digit = 15

list_ = [{'bin': bin(number),
          'dec': number,
          'hex': hex(number),
          'oct': oct(number)} for number in range(numbers_digit+1)]

pprint(list_)
