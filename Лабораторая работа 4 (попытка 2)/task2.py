def get_count_char(str_):
    str_ = str_.lower()
    main_dict = {}
    for letter in str_:
        if letter.isalpha():
            if letter in main_dict:
                main_dict[letter] += 1
            else:
                main_dict[letter] = 1

    return main_dict


def dict_percentages_count(dict_):
    dict_v2 = dict_
    amount = sum(dict_v2.values())
    for letter in dict_v2:
        dict_v2[letter] = (round((dict_v2[letter]*100) / amount, 2))
    return dict_v2


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

counts = get_count_char(main_str)
print(counts)
#percents = dict_percentages_count(counts)
#print(percents)
