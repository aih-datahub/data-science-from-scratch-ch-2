import os; os.system('cls')

# [1] List Items Are Enclosed In Square Brackets
# [2] List Is Ordered, To Use Index To Access Item
# [3] List Is Mutable => Add, Update, Delete
# [4] List Items Is Not Unique
# [5] List Can Has Different Data Types

# -----------------------------------------------------------------------------------------------------------------

list_01 = [1 ,"A" ,"A" ,True, 12.4, False]

print(list_01) # Will get => [1, 'A', True, 12.4, False]


# Indexing And Slicing
# [Start:End:Steps]

print(list_01[1]) # Will get => A
print(type(list_01[1])) # Will get => <class 'str'>

print(list_01[-1]) # Will get => False
print(type(list_01[-1])) # Will get => <class 'bool'>

print(list_01[-1*len(list_01)]) # Will get => 1
print(type(list_01[-1*len(list_01)])) # Will get => <class 'int'>

print(list_01[-3]) # Will get => True
print(type(list_01[-3])) # Will get => <class 'bool'>

print(list_01[1:4]) # Will get => ['A', 'A', True]
print(type(list_01[1:4])) # Will get => <class 'list'>

print(list_01[:4]) # Will get => [1, 'A', 'A', True]
print(type(list_01[:4])) # Will get => <class 'list'>

print(list_01[1:]) # Will get => ['A', 'A', True, 12.4, False]
print(type(list_01[1:])) # Will get => <class 'list'>

print(list_01[0::2]) # Will get => [1, 'A', 12.4]
print(type(list_01[1:])) # Will get => <class 'list'>

# print(list_01[100]) # Will get => IndexError: list index out of range

print("-=-" * 50)

# -----------------------------------------------------------------------------------------------------------------

# Mutable => (Update, Delete) Without Functions

list_02 = [1, 2, 3, False, "A", "B", True, "C", False, 12.41]

print(list_02) # Will get => [1, 2, 3, False, 'A', 'B', True, 'C', False, 12.41]
list_02[3] = "Ahmed" # => Update Operation
print(list_02) # Will get => [1, 2, 3, 'Ahmed', 'A', 'B', True, 'C', False, 12.41]

list_02[3:6] = ["ASD"] # => Update Operation
print(list_02) # Will get => [1, 2, 3, 'ASD', True, 'C', False, 12.41]

list_02[0:3] = [] # Delete Operation
print(list_02) # Will get => ['ASD', True, 'C', False, 12.41]

# -----------------------------------------------------------------------------------------------------------------

# Methods
# Mutable => Add, Update, Delete

list_03 = ["ahmed", 2]

# append() => To add new element
list_03.append(True)
print(list_03) # Will get => ['ahmed', 2, True]

list_04 = [1, 2, 3, 4, 5, 6]
list_03.append(list_04)
print(list_03) # Will get => ['ahmed', 2, True, [1, 2, 3, 4, 5, 6]]


# extend() => As append but when put list will extend old list wit new
list_05 = [1, 2, 3]
list_06 = ["a", "b", "c"]
list_05.extend(list_06)
print(list_05) # Will get => [1, 2, 3, 'a', 'b', 'c']

# remove() => To delete element from list
list_07 = [11, 2, "A", True, "asd", 43]
list_07.remove("A")
print(list_07) # Will get => [1, 2, True, 'asd', 43]
# list_07.remove("a")
# print(list_07) # Will get => list_07.remove("a") ValueError: list.remove(x): x not in list


# sort() => to arrange list has just numbers or just strings
list_08 = [5, 0, -4, 345.2, 23]
list_08.sort()
print(list_08) # Will get => [-4, 0, 5, 23, 345.2]

list_08.sort(reverse=True)
print(list_08) # Will get => [345.2, 23, 5, 0, -4]


# reverse() => To reverse the list order
list_09 = ["dfds", 2, 5, "a", True]
list_09.reverse()
print(list_09) # Will get => [True, 'a', 5, 2, 'dfds']


# clear() => To remove all items from the list
list_10 = [1, 2, 3]
list_10.clear()


# copy() => To copy the list
list_11 = [1, 2, 3, 4]
list_12 = list_11
list_11.append(5)
print(list_12) # Will get => [1, 2, 3, 4, 5] 
# Will edit in the tow list because they are refers the same location in memory to solve this we use copy function
list_13 = [1, 2, 3, 4]
list_14 = list_13.copy()
list_13.append(5)
print(list_14) # Will get => [1, 2, 3, 4]


# count() => to know how many the same item in list
list_15 = [1, 2, 3, 4, 2, 1, 2, 2, 1]
print(list_15.count(1)) # Will get => 3


# index() => to know index of the first item in list
list_16 = [2, 3, 5, 3, 3, 1, 9, 1]
print(list_16.index(1)) # Will get => 5
# print(list_16.index("a")) # Will get => ValueError: 'a' is not in list


# insert() => to add new item to list before specific index
list_17 = ["as", 2, True, 21.4, "sd"]
list_17.insert(2, "Ahmed")
print(list_17) # Will get => ['as', 2, 'Ahmed', True, 21.4, 'sd']
list_17.insert(-1, "Alhopi")
print(list_17) # Will get => ['as', 2, 'Ahmed', True, 21.4, 'Alhopi', 'sd']


# pop() => remove the item from list and return it
list_18 = ["Ahmed", 1, " - ", 65, "Alhopi"]

print(list_18.pop()) # Will get => Alhopi
print(list_18) # Will get => ['Ahmed', 1, ' - ', 65]

print(list_18.pop(2)) # Will get =>  -
print(list_18) # Will get => ['Ahmed', 1, 65]

print(list_18.pop(-1)) # Will get => 65
print(list_18) # Will get => ['Ahmed', 1]

