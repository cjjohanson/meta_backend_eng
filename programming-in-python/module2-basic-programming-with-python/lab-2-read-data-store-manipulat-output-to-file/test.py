with open('sampletext.txt', mode='r') as file:
    data = file.read()

print(data)
print(data.split('\n')[0])