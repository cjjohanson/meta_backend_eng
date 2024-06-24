family = ['Yusra', 'Lana', 'Pinkie', 'CJ']

def find_person(name):
    if name[0].lower() == 'y':
        return name

# map 
print('Map -------')
map_name = map(find_person, family)
for x in map_name:
    print(x)

# filter
print('Filter ----')
filter_name = filter(find_person, family)
print(list(filter_name))
