
# non pure function
my_list = [1, 2, 3]

# def add_to_list(item):
#     my_list.append(item)

# add_to_list(4)
# print(my_list)

# pure function

def new_add_to_list(item, lst):
    lst_copy = lst.copy()
    lst_copy.append(item)
    return lst_copy

print(f"non pure function output: {my_list}")
print(f"pure function output: {new_add_to_list(5, my_list)}")
