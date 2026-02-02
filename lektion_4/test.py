numbers = [3, 1, 4, 2, 5, 2]
empty_list = []

for number in numbers:
    if number not in empty_list:
        empty_list.append(number)
    else:
        print(number)