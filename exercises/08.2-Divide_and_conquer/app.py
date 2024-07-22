list_of_numbers = [4, 80, 85, 59, 37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]

# Your code here
def sort_odd_even(list):
    sorted_list = []
    even = []
    for x in list:
        if x % 2 != 0:
            sorted_list.append(x)
        elif x % 2 == 0:
            even.append(x)
    for z in even:
        sorted_list.append(z)
    return sorted_list


print(sort_odd_even(list_of_numbers))

