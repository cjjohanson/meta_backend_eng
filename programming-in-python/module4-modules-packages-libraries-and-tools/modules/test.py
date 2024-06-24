
# import math
# import sample_library
# import sys

# print('testing')
# print(f"Pi = {math.pi}")


# # import a module from a different directory

# # 1 represents the index of the path where the directory will be inserted. the 0th index
# # represents the current index so add the given path to 1 means "after looking in the current
# # directory, look HERE"
# sys.path.insert(1, r'/Users/cjjohanson/Documents/GitHub/meta_backend_eng/programming-in-python/module4-modules-packages-libraries-and-tools/modules/other_module_directory')
# # yellow squiggly line is there because the IDE doesn't recognize the module but the system does
# # meaning this will still run fine
# import family_names

# print(family_names.family_names)

x = 10

print(id(x))
def func(a):
    y = 4
    print(id(y))
    pass