import numpy as np

# all about strings
print(f'all about strings')
name = "Viky Bad"
print(f'hello, {name}')
print(f'name: {name}')
print(f'''Slicing:
        {name[2]}
        {name[2:3]}
        {name[::-1]}
        {name[::2]}''')
print(f'count/length: {len(name)}')
print(f'replace: {name.replace("Viky", "Vikram")}')

# all about lists
print(f'\n\nall about lists')

names = ['Viky', "Pooja", "Vishal"]
restNames = ["Suyash", "Rohan"]
print(f'list length: {len(names)}')
print(f'reverse a list: {names[::-1]}')
names.append(name)
names.append(restNames)
print(f'append list: {names}')
names.insert(2, "VijayShree")
print(f'insert in list: {names}')
names.pop(3)
print(f'pop index 3 from list: {names}')
names.remove("Pooja")
print(f'removed Pooja from list: {names}')
names1 = [["Viky", "Pooja"], ["Suyash", "Vishal"]]
names1 = list(np.concatenate(names1))
print(f'flatten a list using numpy: {names1}')

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
count = fruits.count('apple')
print(f'Count of apples: {count}')
index = fruits.index('banana')
print(f'Index of banana in list: {index}')
index = fruits.index('banana', 4)
print(f'Find next banana starting a position 4: {index}')
fruits.reverse()
print(f'Reverse the list: {fruits}')
fruits.sort()
print(f'Sort list: {fruits}')
print(f'removes last value of list: {fruits.pop()}')
print(f'removes any index value of list: {fruits.pop(2)}')
matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        (9, 10, 11, "12"),
        ]
d = [[row[i] for row in matrix] for i in range(4)]
print(f'convert 2D-Array to 1D: {d}')
d = [row[i] for row in matrix for i in range(4)]
print(f'flatten a 2d array: {d}')


# all about sets
print(f'\n\nall about sets')

basket = {'apple', 'mango', 'grapes', "apple", "Apple"}
print(f'set basket: {basket}')
print(f'apple in basket: {"apple" in basket}')
print(f'apple not in basket: {"apple" not in basket}')


# all about dictionaries
print(f'\n\nall about dictionaries')

marks = {'Viky': 88, "Pooja": 89, "Sahil": 78}
print(f'marks of Viky: {marks["Viky"]}')

