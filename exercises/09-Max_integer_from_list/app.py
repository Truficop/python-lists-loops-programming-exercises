my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

# Your code here
def max_integer(list):
    max_number = 0
    for x in list:
        if x > max_number:
            max_number = x
    return max_number

print(max_integer(my_list))