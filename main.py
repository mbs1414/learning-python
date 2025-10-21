# 1. Data Types and Basic Operations
num_1 = 5       # integer
num_2 = 5.5     # float
num_3 = 5j      # complex

lastName = "babakhani"

# Priority of math operations:
# 1. ()  2. **  3. * /  4. + -

print(type(num_1))  # <class 'int'>

division = 8 / 4    # 2.0
remainder = 9 % 2   # 1

# Type casting: int(), float(), str()
round(5.555, 2)     # 5.56
# ----------------------------------------------------------------------

# 2. Strings
print("my name is 'mohammad'")    # my name is 'mohammad'
print("my name is \"mohammad\"")  # my name is "mohammad"
print("firstName \n lastName")    # firstName 
                                  #  lastName

"mohammad" + " " + "babakhani"    # 'mohammad babakhani'

f"mohammad {lastName}"            # 'mohammad babakhani'
# ----------------------------------------------------------------------

# 3. Input and Conditionals
# Suppose input = 1
rank = int(input("Enter your rank: "))  # e.g., user enters 1

if rank == 1:
    print("Gold")   # Gold
elif rank == 2:
    print("Silver")
elif rank == 3:
    print("Bronze")
else:
    print("None")

# Shorthand if-else
print("Gold") if rank == 1 else print("None")  # Gold
# ----------------------------------------------------------------------

# 4. Comparison and Logical Operators
obj_1 = ["A"]
obj_2 = list(obj_1)

obj_1 == obj_2  # True
obj_1 is obj_2  # False
# ----------------------------------------------------------------------

# 5. Loops
for item in range(1, 5):
    print('*' * item)
# *
# **
# ***
# ****

# Nested loops with conditions
for item in range(1, 3):
    if item % 2 == 1:
        for star in range(1, 3):
            print('*' * star)
    else:
        for star in range(3, 0, -1):
            print('*' * star)
# *
# **
# ***
# **
# *

# While loop
num = 1
while num <= 10:
    print(num)
    num += 1
# 1 2 3 4 5 6 7 8 9 10
# ----------------------------------------------------------------------

# 6. Lists
list_1 = ['python', 'react', 'javascript']
print(len(list_1))            # 3
print('python' in list_1)     # True

for item in list_1:
    print(item)
# python
# react
# javascript

list_1.append('JS')           # ['python', 'react', 'javascript', 'JS']
list_1.extend(['vue', 'nuxt'])# ['python', 'react', 'javascript', 'JS', 'vue', 'nuxt']
list_1.insert(1, 'next')      # ['python', 'next', 'react', 'javascript', 'JS', 'vue', 'nuxt']
list_1.pop()                  # removes 'nuxt'
list_1.pop(0)                 # removes 'python'
list_1.remove('vue')          # removes 'vue'
list_1.sort()                 # sorted ascending
list_1.reverse()              # reversed order

", ".join(list_1)             # 'react, next, javascript, JS' (example output after sort+reverse)

list_1 = [1, 2, 3, 4, 5]
list_1[1:3]                   # [2, 3]
list_1[:3]                    # [1, 2, 3]
list_1[::2]                   # [1, 3, 5]
list_2 = list_1[:]            # [1, 2, 3, 4, 5]
list_1 is list_2              # False

list_2 = [num * 2 for num in list_1]  # [2, 4, 6, 8, 10]
# ----------------------------------------------------------------------

# 7. Dictionaries
dict_1 = {"name": "mohammad", "age": 24}
print(dict_1.keys())          # dict_keys(['name', 'age'])
print(dict_1.values())        # dict_values(['mohammad', 24])
print("name" in dict_1)       # True
print("mohammad" in dict_1.values())  # True

dict_1.copy()                 # {'name': 'mohammad', 'age': 24}
dict_1.clear()                # {}
dict_1.get("name")            # None
dict_1.pop("name", "Not Found")   # 'Not Found'
dict_1.popitem()              # removes last key-value (if exists)
dict_1.update({"name": "Liza"})  # {'name': 'Liza'}

dict_3 = {}.fromkeys(["name"], "unknown")  # {'name': 'unknown'}

dict_4 = dict(first=1, second=2, third=3)
squared = {key: value ** 2 for key, value in dict_4.items()}  
# {'first': 1, 'second': 4, 'third': 9}
even_odd = {num: ("even" if num % 2 == 0 else "odd") for num in [1,2,3,4,5]}  
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}
# ----------------------------------------------------------------------

# 8. Tuples
tuple_1 = (1, 2, 3)
print(tuple_1[0])     # 1
print(3 in tuple_1)   # True

location = {(35.67, 45.78): "Tehran"}
print(location[(35.67, 45.78)])  # Tehran
# ----------------------------------------------------------------------

# 9. Sets
set_1 = {1, 2, 3, 4}
set_1.add(5)          # {1, 2, 3, 4, 5}
set_1.remove(2)       # {1, 3, 4, 5}
set_1.discard(5)      # {1, 3, 4}
set_1.copy()          # {1, 3, 4}
set_1.clear()         # set()

PY = {"mohammad", "reza"}
JS = {"reza", "nader"}

print(PY | JS)  # {'reza', 'nader', 'mohammad'}
print(PY & JS)  # {'reza'}
# ----------------------------------------------------------------------

# 10. String Formatting in Loops
for item in ["PY", "JS"]:
    print(item, end="-")
    print(item, sep="-")
# PY-PYPY-JSJS-
# ----------------------------------------------------------------------

# 11. Match Statement (Python 3.10+)
response_code = 201
match response_code:
    case 200:
        print("OK")
    case 201:
        print("Created")  # Created
# ----------------------------------------------------------------------

# 12. Functions
def printSomething(something):
    print(something)

printSomething("hello")  # hello

def add(number):
    return number + 6
add(5)  # 11

def hi(word="hi"):
    print(word)
hi("hello")  # hello

def plus(*args):
    total = 0
    for arg in args:
        total += arg
    print(total)
plus(1, 2, 3, 4)  # 10

def show_kwargs(**kwargs):
    print(kwargs)
show_kwargs(name="mohammad")  # {'name': 'mohammad'}

short_version = lambda num: print(num)
short_version(5)  # 5
# ----------------------------------------------------------------------

# 13. Built-in Functions
list_1 = [1, 2, 3, 4]
print(list(map(lambda n: n*n, list_1)))     # [1, 4, 9, 16]
print(list(filter(lambda n: n%2==0, list_1)))  # [2, 4]
all([True, True, True])   # True
any([False, True])        # True

list_2 = [5, 6, 7, 8]
print(list(zip(list_1, list_2)))  # [(1, 5), (2, 6), (3, 7), (4, 8)]
print(dict(zip(list_1, list_2)))  # {1: 5, 2: 6, 3: 7, 4: 8}
# ----------------------------------------------------------------------

# 14. Errors and Debugging
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")   # Cannot divide by zero.
else:
    print("No error occurred.")
finally:
    print("Execution finished.")      # Execution finished.

# pdb example (interactive)
import pdb
pdb.set_trace()
# (Pdb) n        next line
# (Pdb) s        step into function
# (Pdb) c        continue execution
# (Pdb) q        quit debugger
# (Pdb) l        list source lines
# (Pdb) p var    print variable value
# (Pdb) pp var   pretty print variable
# (Pdb) b 12     set breakpoint at line 12
# (Pdb) cl       clear all breakpoints
# (Pdb) w        where (show stack trace)
# (Pdb) u        move up in stack
# (Pdb) d        move down in stack
# (Pdb) a        show function arguments
# (Pdb) !cmd     execute Python command
# ----------------------------------------------------------------------

# 15. Modules and Imports
import random
from random import randint, choices
import termcolor

print(termcolor.colored("python course", color="blue", attrs=["blink"]))
# prints "python course" in blue blinking text
print(__name__)  # __main__
# ----------------------------------------------------------------------

# 16. Object-Oriented Programming (OOP)
class User:
    name = "mohammad"
    familyName = "babakhani"
    
    def showFullName(self):
        return f"{self.name} {self.familyName}"

user_1 = User()
print(user_1.showFullName())  # mohammad babakhani

class User_1:
    def __init__(self, userName):
        self.name = userName
    
    def showName(self):
        return self.name

Ali = User_1("Ali")
print(Ali.showName())  # Ali

class Test:
    _email = "protected"
    __email = "private"

print(dir(Test))
# Output includes: 
# ['_Test__email', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', 
# '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', 
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
# '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_email']
