my_numbers = [2, 4, 5, 10, 7]

def times_two(numbers):
    new_list = []
    for i in numbers:
        new_number = i * 2
        new_list.append(new_number)
    return new_list

bigger_list = times_two(my_numbers)
print(bigger_list)

