name = input("What's your name? ")

# file = open('practice/names.txt', 'a')
# file.write(f'{name}\n')
# file.close()

# with automatically closes the file
with open("practice/names.txt", "a") as file:
    file.write(f"{name}\n")

with open("practice/names.txt", "r") as file:
    names = file.readlines()

print('names: ', names)
for name in sorted(names, key=lambda x: x.lower()):
    print(name.strip())