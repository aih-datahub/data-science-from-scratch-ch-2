import os; os.system('cls')

# [1] Set Items Are Enclosed in Curly Braces {}
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing and Slicing Cant Be Done
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# [5] Set Items Is Unique

# Not Ordered And Not Indexed
set_01 = {1, 2, 3, "Ahmed", True, 32.1, (1, "Alhopi")}
print(set_01) # Will get => {32.1, 1, 2, 3, 'Ahmed', (1, 'Alhopi')}
# print(set_01[1]) # Will get => TypeError: 'set' object is not subscriptable
# print(set_01[0:1]) # Will get => TypeError: 'set' object is not subscriptable


# Has Only Immutable Data Types
# set_02 = {1, 2, [31, 4]} # Will get => TypeError: unhashable type: 'list' 

# Items Is Unique
set_03 = {1, 2, 3, 1, 2, 3}
print(set_03) # Will get => {1, 2, 3}


# -----------------------------------------------------------------------------------------------------------------

# Methods

# clear() => remove all items
set_04 = {1, 2, 3}
set_04.clear()
print(set_04) # Will get => set()


# union() => create one set from sets others to create a new set has all items of sets
set_05 = {"One", "Two", "Three"}
set_06 = {"1", "2", "3"}
set_07 = {"Zero", "Cool"}
print(set_05 | set_06) # Will get => {'One', 'Two', '2', 'Three', '3', '1'}
print(set_05.union(set_06, set_07)) # Will get => {'Zero', 'One', 'Cool', 'Two', '2', 'Three', '3', '1'}


# add() => insert new item
set_08 = {1, 2, 3, 4}
set_08.add(5)
set_08.add(6)
print(set_08) # Will get => {1, 2, 3, 4, 5, 6}


# copy() => to take a shallow copy of a set
set_09 = {1, 2, 3, 4}
set_10 = set_09.copy()
print(set_09) # Will get => {1, 2, 3, 4}
print(set_10) # Will get => {1, 2, 3, 4}
set_09.add(6)
print(set_09) # Will get => {1, 2, 3, 4, 6}
print(set_10) # Will get => {1, 2, 3, 4}


# remove() => delete item from set and if not found will return KeyError
set_11 = {1, 2, 3, 4}
set_11.remove(1)
print(set_11) # Will get => {2, 3, 4}
# set_11.remove(7) # Will get => KeyError: 7


# discard() => as remove function but if item not found don't return error
set_12 = {1, 2, 3, 4}
set_12.discard(1)
print(set_12) # Will get => {2, 3, 4}
set_12.discard(7)


# pop() => return random item and delete it
set_13 = {"A", True, 1, 2, 3, 4, 5}
print(set_13.pop()) # Will get => True
print(set_13) # Will get => {2, 3, 4, 5, 'A'}
print(set_13.pop()) # Will get => 2
print(set_13) # Will get => {3, 4, 5, 'A'}

set_test_01 = {1, 2, 1, 2, 1, 2}
print(set_test_01.pop()) # Will get => 1
print(set_test_01) # Will get => {2}

# update() => as add but this can add many items in the same command
set_14 = {1, 2, 3}
set_15 = {1, "A", "B", 2}
set_14.update(['Html', "Css"])
set_14.update(set_15)
print(set_14) # Will get => {1, 2, 3, 'Html', 'Css', 'A', 'B'}


# difference() or - => return the items that it in first set and not found in the second set
set_16 = {1, 2, 3, 4}
set_17 = {1, 2, 3, "Osama", "Ahmed"}
print(set_16) # Will get => {1, 2, 3, 4}
print(set_16.difference(set_17)) # Will get => {4}
print(set_16 - set_17) # Will get => {4}
print(set_16) # Will get => {1, 2, 3, 4}


# difference_update() => as difference function but store the result in first set
set_18 = {1, 2, 3, 4}
set_19 = {1, 2, "Osama", "Ahmed"}
print(set_18) # Will get => {1, 2, 3, 4}
set_18.difference_update(set_19) # set_18 = set_18 - set_19
print(set_18) # Will get => {3, 4}


# intersection() or & => return the items that found in first set and second set
set_20 = {1, 2, 3, 4, "X", "Osama"}
set_21 = {"Osama", "X", 2}
print(set_20) # Will get => {1, 2, 3, 4, 'Osama', 'X'}
print(set_20.intersection(set_21)) # Will get => {'X', 2, 'Osama'}
print(set_20 & set_21) # Will get => {'X', 2, 'Osama'}
print(set_20) # Will get => {1, 2, 3, 4, 'Osama', 'X'}


# intersection_update() => as intersection function but store the result in first set
set_22 = {1, 2, 3, 4, "X", "Osama"}
set_23 = {"Osama", "X", 2}
print(set_22) # Will get => {1, 2, 3, 4, 'Osama', 'X'}
set_22.intersection_update(set_23) # set_22 = set_22 & set_23
print(set_22) # Will get => {'Osama', 'X', 2}


# symmetric_difference() or ^ => return the items that in first set and not found in 
# the second and items in the second and not found in the first
set_24 = {1, 2, 3, 4, 5, "X"}
set_25 = {"Osama", "Zero", 1, 2, 4, "X"}
print(set_24) # Will get => {1, 2, 3, 4, 5, 'X'}
print(set_24.symmetric_difference(set_25)) # Will get => {'Osama', 'Zero', 3, 5}
print(set_24 ^ set_25) # Will get => {'Osama', 'Zero', 3, 5}
print(set_24) # Will get => {1, 2, 3, 4, 5, 'X'}


# symmetric_difference_update() => as symmetric_difference but the result will store in the first set
set_26 = {1, 2, 3, 4, 5, "X"}
set_27 = {"Osama", "Zero", 1, 2, 4, "X"}
print(set_26) # Will get => {1, 2, 3, 4, 5, 'X'}
set_26.symmetric_difference_update(set_27) # set_26 = set_26 ^ set_27
print(set_26) # Will get => {'Zero', 3, 5, 'Osama'}


# issuperset() => return True if the all items in second set are found in the first set or return False
set_28 = {1, 2, 3, 4}
set_29 = {1, 2, 3}
set_30 = {1, 2, 3, 4, 5}
print(set_28.issuperset(set_29)) # Will get => True
print(set_28.issuperset(set_30)) # Will get => False


# issubset() => return True if the all items in first set are found in the second set or return False
print(set_28.issubset(set_29)) # Will get => False
print(set_28.issubset(set_30)) # Will get => True


# isdisjoint() => return True if all items in second not found in first set or return False
set_31 = {1, 2, 3, 4}
set_32 = {1, 2, 3}
set_33 = {10, 11, 12}
print(set_31.isdisjoint(set_32)) # Will get => False
print(set_31.isdisjoint(set_33)) # Will get => True







