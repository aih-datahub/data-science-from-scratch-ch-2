import os; os.system("cls")

# [1] Tuple Items Are Enclosed in Parentheses
# [2] You Can Remove The Parentheses If You Want
# [3] Tuple Are Ordered, To Use Index To Access Item
# [4] Tuple Are Immutable => You Cant Add or Delete
# [5] Tuple Items Is Not Unique
# [6] Tuple Can Have Different Data Types
# [7] Operators Used in Strings and Lists Available In Tuples

tuple_01 = (1, 2, True, "Ahmed", 22.4, [1, 2, 3], 1, 1, 1, 2)
tuple_02 = 1, 2, True, "Ahmed", 22.4, [1, 2, 3], 1, 1, 1, 2
tuple_03 = (1, )
tuple_04 = 1,
print(tuple_01) # Will get => (1, 2, True, 'Ahmed', 22.4, [1, 2, 3], 1, 1, 1, 2)
print(tuple_02) # Will get => (1, 2, True, 'Ahmed', 22.4, [1, 2, 3], 1, 1, 1, 2)
print(tuple_03) # Will get => (1,)
print(tuple_04) # Will get => (1,)
print(type(tuple_01)) # Will get => <class 'tuple'>
print(type(tuple_02)) # Will get => <class 'tuple'>
print(type(tuple_03)) # Will get => <class 'tuple'>
print(type(tuple_04)) # Will get => <class 'tuple'>

print(tuple_01[0]) # Will get => 1
print(tuple_01[3]) # Will get => Ahmed
print(tuple_01[-1]) # Will get => [1, 2, 3]

# tuple_01[4] = "Alhopi" # Will get => TypeError: 'tuple' object does not support item assignment
# tuple_01[4] = [] # Will get => TypeError: 'tuple' object does not support item assignment


# Tuple Concatenation

tuple_05 = (1, 2, 3, 4)
tuple_06 = (5, 6)
tuple_07 = tuple_05 + tuple_06
tuple_08 = tuple_05 + ("A", "B", True) + tuple_06
print(tuple_07) # Will get => (1, 2, 3, 4, 5, 6)
print(tuple_08) # Will get => (1, 2, 3, 4, 'A', 'B', True, 5, 6)


# Tuple, List, String Repeat (*)

str_01 = "Ahmed"
list_01 = [1, 2]
tuple_09 = ("A", "B")
print(str_01 * 6) # Will get => AhmedAhmedAhmedAhmedAhmedAhmed
print(list_01 * 6) # Will get => [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
print(tuple_09 * 6) # Will get => ('A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B')


# Methods => count()

tuple_10 = (1, 3, 7, 8, 2, 8, 5, 8)
print(tuple_10.count(8)) # Will get => 3


# Methods => index()

tuple_11 = (1, 3, 7, 8, 2, 6, 5)
print(tuple_11.index(7)) # Will get => 2


# Tuple Destruct

tuple_12 = ("A", "B", 4, "C")

str_02, str_03, _, str_04 = tuple_12

print(str_02) # Will get => A
print(str_03) # Will get => B
print(str_04) # Will get => C


