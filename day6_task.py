#1. Write a python program to remove an item from a tuple

tuple_1 = ("hello", 25, 's', 2+6j)
print(tuple_1)

tuple_1 = tuple_1[:2] + tuple_1[3:]
print(tuple_1)

"""
2. Create a dict as
 a={1:"a",2:"b"}
And add item 3:"4" using update().
"""

Dict = {
    1: 'a',
    2: 'b'
    }
print(Dict)

Dict.update({3:"4"})
print(Dict)

#3. Write a python program to find the length of a set

myset = {"hello", 25, 2.5, "world"}
print(myset)
print(len(myset))




