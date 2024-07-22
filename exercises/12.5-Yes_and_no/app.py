the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here

def change_value(number):
    changed_number = ''
    if number == 0:
        changed_number = 'woko'
    elif number == 1:
        changed_number = 'wiki'
    return changed_number

new_list = list(map(change_value, the_bools))
print(new_list)