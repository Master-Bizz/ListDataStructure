# List items are enclosed in square brackets
# Lists are ordered
# Lists are mutable - things can be changed/replaced
# List elements do not need to be unique.
# Elements can be of different data types.
'''
List Indexing
'''
#num1 = input('insert an int: ')
#num2 = input('insert any float: ')
#result = int(num1) * float(num2)
#print(result)
#-------------------------------------------------------------
# list = []
# list = [1,2,3]
# list = ['apple', 'pear', 'orange']
# list = [3, "coolio", 34.76]
# print(list)
# By default python will print the latest list made
# print(list[2])
# print(list[0:1])
#-------------------------------------------------------------
# A List within a list
# list = ["nuff", "coolio", "nice", ['apple', 'pear', 'tangerine']]
# print(list[1])
# print(list[2][2])
# print(list[3][2])
# print(list[3][2][0])
'''
How to Slice Lists in Python
'''
# list = ['apple', 'pear', 'orange', 'tangerine']
# print(list[1:3])
# print(list[1:4])
# print(list[1:-2])
# print(list[1:-3])
# print(list[:-2])
# print(list[:3])
# print(list[3])
# print(list[::3])
# print(list[::30])

'''
Add Elements To a List
'''
# Change something
# list = ['apple', 'pear', 'orange', 'tangerine']
# list[0] = "Plum"
# print(list)

# Replace something
# list[1:4] = ['Berry', 'Blueberry', 'Blackberry', 'Strawberry']
# print(list)

# Add something
# list.append('Rasberry')
# print(list)
'''
Remove or Delete List Items
'''
# list = ['Berry', 'Blueberry', 'Blackberry', 'Strawberry']
# del list[2]
# print(list)
# list.append('Lime')
# print(list)
# del list[1:2]
# print(list)
# del list
# print(list)

'''
Python List Methods
'''
print(dir(list))  # directory of what you can do with list
print(help(list.clear)) # function explains what you can do

# fruits = ['Lime', 'Juice', 'Bannana', 'Pineapple']
# fruits.insert(1, 'Cherry')
# print(fruits)

# fruits.pop(1) # pop takes away
# print(fruits)
# fruits.append('Cherry')

# bye = fruits.index("Juice")
# fruits.pop(bye)
# print(fruits)
#======================================================

# fruits = ['Lime', 'Juice', 'Bannana', 'Pineapple', 'Juice']
# print(fruits.count('Juice'))   # Count - finding the mode
# print(fruits)

# result = {}
# for n in fruits:
   # result[n] = fruits.count(n)
# print(result)


#import collections

#from collections import counter
#print(counter(fruits))

"""
List Membership Test
"""

fruits = ['Lime', 'Juice', 'Bannana', 'Pineapple', 'Juice']
print('Lime' in fruits)
print('Lime' not in fruits)
print('Cake' not in fruits)