import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(input_file, delimiter=",") -> list[dict]:
    with open(input_file) as file:
        data = [str_ for str_ in file]
        new_data_lists = [(line.strip()).split(delimiter) for line in data]
        last_data = []
        for i in range(1, len(new_data_lists)):
            new_dict = {}
            for j in range(len(new_data_lists[0])):
                new_dict.update({new_data_lists[0][j]: new_data_lists[i][j]})
            last_data.append(new_dict)
        return last_data


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
