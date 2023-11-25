nice = [1,2,3,4,5,6]

wow = [print(x) for x in nice]

# python kewords
# in, False, True, try, if, except, finally, for, from, global, or, pass etc

# build in data types in python
# text type str
# numerical type int float, complex
# mapping dict
# set types set, frozenset
# boolean type bool
# binary types bytes,bytearray
# None type None types 

# Differnent between python list and arrays
# both list and arrys are used to store collection of items
# they can index,iterating etc
# list item are enclosed in [] they are mutable, duplication is possible, compain string, integers etc
# eg of list ["8.9",8,"hello"]

# Array -orderd, mutable,etc
import array as ar
my = ar.array("i",[1,2,3,4,5])
print(type(my))
print(my[1])

import numpy as np
my_arr = np.array(["hello",1,2,4])
print(my_arr)

# arrays need to be declared 
# arrys can store data very compacitly
# arrays are great for numericald operations

j = [1,2,3,4,5,6,5]
j.append(1)
y = j.copy()
j.clear()
# for x in range(len(y)):
#     print(y.pop())

# Python dictionary is an unorderd items, Each item of a dictionary has a key value pair
# can't indices lke in other types like list and types

my_dict = {
    "key":"value1",
    "key2":"value2"
}

print(my_dict.keys())

my_dicty = dict([(1,"apple"),(2,"banana"),(3,"grapes")])
print(my_dicty.keys())
print(my_dicty[1])

lis = ["a","c","d","j","f","b","g","e","i","h"]
lis = sorted(lis,reverse=True)
print(lis)


# sliceing in python
print(lis[:3])
print(lis[3:])

# diffrence btwn list and tuple
# list are mutable, tuple are not cn't change

# python build in functions
# list(), abs(), set(), len(), dir(), float(), int(), open(), range(), sum(), zip()

# print(abs(-24.4))

# explain modules and packages in python
# module is python file which contail python file extention ".py"
# contains funcitons, classes etc helps to reduse the usage of reusing of same lines
# eg calc.py file has add, sub, mul, div functions which is reusable , simply callable by import calc


# lots of modules in a directory callde package

revstring = "leo"
res = ""
for x in revstring:
    # l,el,oel
    res = x + res
print(res)

ni = "".join(reversed(revstring))
print(ni)

# new = slice(0::)
print(revstring[::-1])