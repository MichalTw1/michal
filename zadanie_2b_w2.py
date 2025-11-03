five_numbers = [2, 5, 6, 8, 9]

def times_two(numbers):
    new_numbers = [i * 2 for i in numbers]
    return new_numbers

bigger_list = times_two(five_numbers)
print(bigger_list)