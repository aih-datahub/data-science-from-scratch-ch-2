import os; os.system("cls")

# [1] Dict Items Are Enclosed in Curly Braces
# [2] Dict Items Are Contains Key : Value
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique
# [6] Dict Is Not Ordered You Access Its Element With Key


dict_01 = {
  "name": "Ahmed",
  "age": 24,
  "country": "Palestine",
  "skills": ["Python", "PHP", "Ropy"],
  "rating": 9.8,
  (1,2,3): "AnyThing"
}
print(dict_01) # Will get => {'name': 'Ahmed', 'age': 24, 'country': 'Palestine', 'skills': ['Python', 'PHP', 'Ropy'], 'rating': 9.8, (1, 2, 3): 'AnyThing'}
print(dict_01["country"]) # Will get => Palestine
print(dict_01.get("country")) # Will get => Palestine
print(dict_01.keys()) # Will get => dict_keys(['name', 'age', 'country', 'skills', 'rating', (1, 2, 3)])
print(dict_01.values()) # Will get => dict_values(['Ahmed', 24, 'Palestine', ['Python', 'PHP', 'Ropy'], 9.8, 'AnyThing'])


# Two-Dimensional Dictionary
dict_02 = {
    "One": {"name": "Html", "progress": "80%"},
    "Two": {"name": "Css", "progress": "90%"},
    "Three": {"name": "Js", "progress": "90%"},
}
print(dict_02) # Will get => {'One': {'name': 'Html', 'progress': '80%'}, 'Two': {'name': 'Css', 'progress': '90%'}, 'Three': {'name': 'Js', 'progress': '90%'}}
print(dict_02["One"]) # Will get => {'name': 'Html', 'progress': '80%'}
print(dict_02["Three"]["name"]) # Will get => Js

# Dictionary Length
print(len(dict_02)) # Will get => 3
print(len(dict_02["Two"])) # Will get => 2


# -----------------------------------------------------------------------------------------------------------------

# Methods

# clear() => Will remove all items
dict_03 = {"name": "Ahmed"}
print(dict_03) # Wil get => {'name': 'Ahmed'}
dict_03.clear()
print(dict_03) # Wil get => {}


# update() => if key found will update the value ,if not will add key and value
dict_04 = {"name": "Ahmed"}
print(dict_04) # Wil get => {'name': 'Ahmed'}
dict_04["age"] = 24
print(dict_04) # Wil get => {'name': 'Ahmed', 'age': 24}
dict_04.update({"country": "Palestine"})
print(dict_04) # Wil get => {'name': 'Ahmed', 'age': 24, 'country': 'Palestine'}


# copy() => to take a shallow copy
dict_05 = {"name": "Ahmed"}
dict_06 = dict_05.copy()
print(dict_06) # Wil get => {'name': 'Ahmed'}
dict_05.update({"skills": "Hacking"})
print(dict_05) # Wil get => {'name': 'Ahmed', 'skills': 'Hacking'}
print(dict_06) # Wil get => {'name': 'Ahmed'}


# setdefault() => to return the value of key and if not found will return the value in function
dict_07 = {"name": "Ahmed"}
print(dict_07) # Wil get => {'name': 'Ahmed'}
print(dict_07.setdefault("age", 24)) # Wil get => 24
print(dict_07) # Wil get => {'name': 'Ahmed', 'age': 24}


# popitem() => return a tuple has tow items for key and value from last item in dictionary
dict_08 = {"name": "Ahmed", "skill": "Running", "age": 24}
print(dict_08) # Wil get => {"name": "Ahmed", "skill": "Running", "age": 24}
print(dict_08.popitem()) # Wil get => ('age', 24)
print(dict_08) # Wil get => {'name': 'Ahmed', 'skill': 'Running'}


# items() => return a list has tuples for all items in dictionary 
dict_09 = {"name": "Ahmed", "skill": "XBox"}
tuple_01 = dict_09.items()
print(dict_09) # Wil get => {'name': 'Ahmed', 'skill': 'XBox'}
dict_09["age"] = 36
print(tuple_01) # Wil get => dict_items([('name', 'Ahmed'), ('skill', 'XBox'), ('age', 36)])


# fromkeys() => return a dictionary from keys and values that passed in function
tuple_02 = ("MyKeyOne", "MyKeyTwo", "MyKeyThree")
str_01 = "X"
dict_10 = {}
dict_10 = dict.fromkeys(tuple_02, str_01)
print(dict_10) # Will get => {'MyKeyOne': 'X', 'MyKeyTwo': 'X', 'MyKeyThree': 'X'}


