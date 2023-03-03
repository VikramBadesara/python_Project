import numpy as np

# all about strings
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

# all about dictionaries