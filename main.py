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

# Protected and Private Attributes
# ---------------------------------------
class Test:
    _email = "protected"   # protected attribute
    __email = "private"    # private attribute (will be name-mangled)

print(dir(Test))
# 🔹 Output: list of all class attributes and methods
# ['_Test__email', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', 
# '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', 
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
# '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_email']
# 🟢 Note: private variable appears as _Test__email (name mangling)

# ---------------------------------------
# Adding attributes and methods dynamically
# ---------------------------------------
class Fruits:
    fruit = "apple"

orange = Fruits()
orange.otherFruits = "orange"   # dynamically adding a new attribute to an instance

def sayHi(self):
    print("Hi")

import types
orange.sayHi = types.MethodType(sayHi, orange)  # dynamically adding a method

orange.sayHi()
# 🔹 Output:
# Hi

# ---------------------------------------
# __repr__ and object representation
# ---------------------------------------
class Sports:
    def __init__(self, sportName):
        self.name = sportName

    def __repr__(self):
        return self.name

football = Sports("Football")
print(football)
# 🔹 Output: Football (because __repr__ returns the name)

# Without __repr__, it would print something like:
# <__main__.Sports object at 0x00000238E4F8A550>

# ---------------------------------------
# Inheritance
# ---------------------------------------
class Basketball(Sports):  # inherits from Sports
    pass

game = Basketball("Basketball")
print(game)
# 🔹 Output: Basketball

# ---------------------------------------
# Using @classmethod
# ---------------------------------------
class Car:
    wheels = 4

    @classmethod # means the method belongs to the class itself, not to an instance.
    def set_wheels(cls, number):
        Car.wheels = number

print(Car.wheels)
# 🔹 Output: 4

Car.set_wheels(6)
print(Car.wheels)
# 🔹 Output: 6 (the class variable changed for all instances)

# ---------------------------------------
# Using @property
# ---------------------------------------
class User:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):         # getter
        return self._name

    def name(self, newName):  # this should be a setter using @name.setter, but it’s incorrect
        self._name = newName

User.name = "Alex"
print(User.name)
# 🔹 Output: Alex
# ⚠️ Note: name is now just a class variable, not a property, because setter was not declared properly.

# ---------------------------------------
# Using super() and inheritance constructor
# ---------------------------------------
class Name:
    def __init__(self, name):
        self.name = name

class FullName(Name):
    def __init__(self, name, familyName):
        super().__init__(name)    # call parent __init__
        self.familyName = familyName

person = FullName("Ali", "Rezaei")
print(person.name, person.familyName)
# 🔹 Output: Ali Rezaei

# ---------------------------------------
# Multiple Inheritance Example
# ---------------------------------------

class Animal:
    def eat(self):
        print("Animal is eating")

class Flyable:
    def fly(self):
        print("This creature can fly")

# Bird inherits from both Animal and Flyable
class Bird(Animal, Flyable):
    def chirp(self):
        print("Bird is chirping")

parrot = Bird()

# Inherited from Animal
parrot.eat()
# 🔹 Output: Animal is eating

# Inherited from Flyable
parrot.fly()
# 🔹 Output: This creature can fly

# Defined in Bird itself
parrot.chirp()
# 🔹 Output: Bird is chirping


# ---------------------------------------
# Method Resolution Order (MRO)
# ---------------------------------------
print(Bird.__mro__)
# 🔹 Output: (<class '__main__.Bird'>, <class '__main__.Animal'>, <class '__main__.Flyable'>, <class 'object'>)
# MRO defines the order in which Python looks for methods in multiple inheritance.


# ---------------------------------------
# isinstance() and issubclass()
# ---------------------------------------

# isinstance(object, class)
print(isinstance(parrot, Bird))
# 🔹 Output: True

print(isinstance(parrot, Animal))
# 🔹 Output: True (because Bird inherits from Animal)

print(isinstance(parrot, Flyable))
# 🔹 Output: True

print(isinstance(parrot, object))
# 🔹 Output: True (everything in Python is derived from object)


# issubclass(child_class, parent_class)
print(issubclass(Bird, Animal))
# 🔹 Output: True

print(issubclass(Bird, Flyable))
# 🔹 Output: True

print(issubclass(Bird, object))
# 🔹 Output: True

print(issubclass(Animal, Flyable))
# 🔹 Output: False (Animal does not inherit from Flyable)

# ---------------------------------------
# Polymorphism Example
# ---------------------------------------

class Animal:
    def make_sound(self):
        # This method is meant to be overridden by subclasses
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

# Different objects, same method name → different behavior
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.make_sound())
# 🔹 Output:
# Woof!
# Meow!
# Moo!


# ---------------------------------------
# Demonstrating NotImplementedError
# ---------------------------------------

class Vehicle:
    def start_engine(self):
        # This is a placeholder for subclasses
        raise NotImplementedError("Subclasses must implement start_engine()")

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

class Bike(Vehicle):
    pass  # No start_engine() implementation

# Car works fine
car = Car()
print(car.start_engine())
# 🔹 Output: Car engine started

# Bike will raise an error
bike = Bike()
try:
    print(bike.start_engine())
except NotImplementedError as e:
    print(f"Error: {e}")
# 🔹 Output: Error: Subclasses must implement start_engine()

# ---------------------------------------
# Dunder (Double Underscore) Methods
# Example: __add__
# ---------------------------------------

# Dunder methods are special methods that start and end with double underscores.
# They allow custom behavior for built-in operators and functions.
# Example: __add__, __len__, __str__, __eq__, __lt__, etc.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Define behavior for the + operator
    def __add__(self, other):
        # Return a new Point object that adds x and y values
        return Point(self.x + other.x, self.y + other.y)

    # Define string representation for printing
    def __str__(self):
        return f"({self.x}, {self.y})"

# Create two Point objects
p1 = Point(3, 5)
p2 = Point(2, 4)

# Use + operator → calls __add__ method automatically
p3 = p1 + p2
print(p3)
# 🔹 Output: (5, 9)

# Same result if called manually:
print(p1.__add__(p2))
# 🔹 Output: (5, 9)

# ---------------------------------------
# Explanation
# ---------------------------------------
# When you write p1 + p2, Python internally does this:
#     p1.__add__(p2)
#
# This is called "Operator Overloading" — redefining the meaning of an operator
# for user-defined objects.


# ---------------------------------------
# Iterable, Iterator, Iteration
# ---------------------------------------

# ✅ Iterable: an object capable of returning its elements one at a time.
# Examples: list, tuple, string, set, dictionary, etc.

numbers = [10, 20, 30]
print(numbers)  
# 🔹 Output: [10, 20, 30]

# You can loop through an iterable with a for loop
for num in numbers:
    print(num)
# 🔹 Output:
# 10
# 20
# 30


# ---------------------------------------
# ✅ Iterator: an object that remembers its state during iteration
# You can create an iterator from an iterable using iter()
# ---------------------------------------

iterator = iter(numbers)  # Convert list (iterable) → iterator

print(iterator)
# 🔹 Output: <list_iterator object at 0x...>

# ---------------------------------------
# ✅ next() function: returns the next item from the iterator
# ---------------------------------------

print(next(iterator))  # 🔹 Output: 10
print(next(iterator))  # 🔹 Output: 20
print(next(iterator))  # 🔹 Output: 30

# Once the iterator is exhausted, calling next() again raises StopIteration
try:
    print(next(iterator))
except StopIteration:
    print("No more items in iterator.")
# 🔹 Output: No more items in iterator.


# ---------------------------------------
# ✅ Iteration process manually (behind the scenes of a for loop)
# ---------------------------------------

names = ["Ali", "Reza", "Sara"]
it = iter(names)

while True:
    try:
        item = next(it)
        print(item)
    except StopIteration:
        break
# 🔹 Output:
# Ali
# Reza
# Sara


# ---------------------------------------
# ✅ Example: Custom Iterator Class
# ---------------------------------------

class CountUpTo:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        # The __iter__ method returns the iterator object itself
        return self

    def __next__(self):
        # Defines what happens when next() is called
        if self.current <= self.limit:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration  # Signals that iteration is finished

counter = CountUpTo(3)
for num in counter:
    print(num)
# 🔹 Output:
# 1
# 2
# 3

# ---------------------------------------
# Custom Iterator Example
# ---------------------------------------

class EvenNumbers:
    def __init__(self, limit):
        # Initialize starting number and limit
        self.limit = limit
        self.number = 0

    def __iter__(self):
        # Returns the iterator object itself
        return self

    def __next__(self):
        # Generate the next even number
        if self.number <= self.limit:
            result = self.number
            self.number += 2
            return result
        else:
            # StopIteration signals that iteration is finished
            raise StopIteration


# ---------------------------------------
# Using the custom iterator
# ---------------------------------------

evens = EvenNumbers(10)

for num in evens:
    print(num)
# 🔹 Output:
# 0
# 2
# 4
# 6
# 8
# 10


# ---------------------------------------
# Using next() manually
# ---------------------------------------

evens = EvenNumbers(6)
iterator = iter(evens)

print(next(iterator))  # 🔹 0
print(next(iterator))  # 🔹 2
print(next(iterator))  # 🔹 4
print(next(iterator))  # 🔹 6
try:
    print(next(iterator))
except StopIteration:
    print("Iteration finished!")
# 🔹 Output: Iteration finished!
