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

# ---------------------------------------
# Generator Function Example
# ---------------------------------------

def count_up_to(limit):
    number = 1
    while number <= limit:
        yield number  # 'yield' turns this into a generator
        number += 1

counter = count_up_to(3)

print(next(counter))  # 🔹 Output: 1
print(next(counter))  # 🔹 Output: 2
print(next(counter))  # 🔹 Output: 3

try:
    print(next(counter))
except StopIteration:
    print("No more numbers!")
# 🔹 Output: No more numbers!

# Or simply iterate:
for num in count_up_to(5):
    print(num)
# 🔹 Output: 1 2 3 4 5

# ---------------------------------------
# 1. Basic Decorator Example
# ---------------------------------------

# A decorator is a function that takes another function as an argument,
# adds some functionality to it, and returns a new function.

def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper


# Apply decorator manually
def say_hello():
    print("Hello!")

decorated_func = my_decorator(say_hello)
decorated_func()
# 🔹 Output:
# Before the function runs
# Hello!
# After the function runs


# ---------------------------------------
# 2. Using @ Syntax (Decorator Shortcut)
# ---------------------------------------

@my_decorator
def greet():
    print("Hi there!")

greet()
# 🔹 Output:
# Before the function runs
# Hi there!
# After the function runs


# ---------------------------------------
# 3. Decorator with Arguments
# ---------------------------------------

def repeat_decorator(func):
    def wrapper(*args, **kwargs):
        print("Running the function twice:")
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

@repeat_decorator
def say_name(name):
    print(f"My name is {name}")

say_name("Mohammad")
# 🔹 Output:
# Running the function twice:
# My name is Mohammad
# My name is Mohammad


# ---------------------------------------
# 4. Decorator that Returns Function Results
# ---------------------------------------

def add_logging(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@add_logging
def add(a, b):
    return a + b

sum_result = add(5, 3)
# 🔹 Output:
# Calling function: add
# Result: 8
# sum_result = 8


# ---------------------------------------
# 5. Multiple Decorators Example
# ---------------------------------------

def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

@bold
@italic
def text():
    return "Python"

print(text())
# 🔹 Output: <b><i>Python</i></b>
# Note: decorators are applied from bottom to top (inside → out)


# ---------------------------------------
# 6. Using functools.wraps (Preserve Original Metadata)
# ---------------------------------------

from functools import wraps

def info_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__} with arguments {args}")
        return func(*args, **kwargs)
    return wrapper

@info_logger
def multiply(a, b):
    """This function multiplies two numbers."""
    return a * b

print(multiply(3, 4))  # 🔹 Output: Running multiply with arguments (3, 4) → 12
print(multiply.__name__)  # 🔹 Output: multiply (without wraps → "wrapper")
print(multiply.__doc__)   # 🔹 Output: This function multiplies two numbers.


# ---------------------------------------
# Generator Comprehension
# ---------------------------------------

# A generator comprehension looks like a list comprehension,
# but uses parentheses () instead of brackets [].
# It creates a generator object that produces items one at a time — lazily.

# ✅ Example 1: Basic generator comprehension
gen = (num * 2 for num in range(5))

print(gen)
# 🔹 Output: <generator object <genexpr> at 0x...>

# You can iterate over it using a for loop
for value in gen:
    print(value)
# 🔹 Output:
# 0
# 2
# 4
# 6
# 8


# ---------------------------------------
# ✅ Example 2: Using next() manually
# ---------------------------------------

gen = (n ** 2 for n in range(3))

print(next(gen))  # 🔹 0
print(next(gen))  # 🔹 1
print(next(gen))  # 🔹 4

# Once exhausted, next() raises StopIteration
try:
    print(next(gen))
except StopIteration:
    print("Generator is finished!")
# 🔹 Output: Generator is finished!


# ---------------------------------------
# ✅ Example 3: Comparing List vs Generator
# ---------------------------------------

# List comprehension creates the entire list in memory
nums_list = [x * 2 for x in range(1000000)]

# Generator comprehension creates values one by one (lazy evaluation)
nums_gen = (x * 2 for x in range(1000000))

import sys
print("List size:", sys.getsizeof(nums_list))
print("Generator size:", sys.getsizeof(nums_gen))
# 🔹 Output (approx):
# List size: 9000112 bytes
# Generator size: 104 bytes


# ---------------------------------------
# ✅ Example 4: Using with sum() or any() directly
# ---------------------------------------

# You can use generator comprehensions directly inside functions
total = sum(x for x in range(5))
print(total)
# 🔹 Output: 10

has_even = any(x % 2 == 0 for x in range(5))
print(has_even)
# 🔹 Output: True


# ---------------------------------------
# Decorators and @wraps
# ---------------------------------------

# A decorator is a function that takes another function as an argument
# and returns a modified version of that function — usually adding extra functionality.

# ---------------------------------------
# ✅ Example 1: Basic Decorator
# ---------------------------------------

def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# 🔹 Output:
# Before the function runs
# Hello!
# After the function runs


# ---------------------------------------
# ✅ Example 2: Problem — Losing Metadata
# ---------------------------------------
# When you wrap a function manually, its __name__ and __doc__ are replaced by the wrapper’s.

print(say_hello.__name__)  # 🔹 Output: wrapper  (not 'say_hello')


# ---------------------------------------
# ✅ Example 3: Fixing it with functools.wraps
# ---------------------------------------

from functools import wraps

def my_decorator(func):
    @wraps(func)  # This preserves metadata of the original function
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@my_decorator
def greet():
    """This function greets the user."""
    print("Hi there!")

greet()
# 🔹 Output:
# Before the function runs
# Hi there!
# After the function runs

print(greet.__name__)  # 🔹 Output: greet
print(greet.__doc__)   # 🔹 Output: This function greets the user.


# ---------------------------------------
# ✅ Example 4: Decorator with Arguments
# ---------------------------------------

def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi(name):
    print(f"Hi, {name}!")

say_hi("Mohammad")
# 🔹 Output:
# Hi, Mohammad!
# Hi, Mohammad!
# Hi, Mohammad!


# ---------------------------------------
# ✅ Example 5: Multiple Decorators
# ---------------------------------------

def bold(func):
    @wraps(func)
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def italic(func):
    @wraps(func)
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@bold
@italic
def text():
    return "Hello!"

print(text())
# 🔹 Output: <b><i>Hello!</i></b>


from functools import wraps  # keeps the original function’s metadata (like __name__, __doc__)

# -----------------------------------------
# 🔹 Decorator Factory Template
# -----------------------------------------

def decorator_factory(arg1, arg2):
    """
    This is a decorator factory.
    It takes arguments (arg1, arg2) and returns a decorator function.
    """

    def actual_decorator(func):
        """
        This is the actual decorator that receives the function to be wrapped.
        """

        @wraps(func)  # keeps the function name and docstring intact
        def wrapper(*args, **kwargs):
            """
            This is the wrapper function that replaces the original one.
            You can run custom logic before and after calling the original function.
            """

            # --- Before the function runs ---
            print(f"Decorator factory arguments: {arg1}, {arg2}")
            print(f"Calling {func.__name__}() with args: {args}, kwargs: {kwargs}")

            # --- Call the original function ---
            result = func(*args, **kwargs)

            # --- After the function runs ---
            print(f"{func.__name__}() returned: {result}")

            return result  # return the original function’s result

        return wrapper  # return the wrapped function

    return actual_decorator  # return the decorator

# -----------------------------------------
# 🔹 Using the Decorator Factory
# -----------------------------------------

@decorator_factory("Hello", "World")  # this calls the factory first
def greet(name):
    """Simple greeting function."""
    return f"Hi, {name}!"

# -----------------------------------------
# 🔹 Execution
# -----------------------------------------

greet("Mohammad")

# Output:
# Decorator factory arguments: Hello, World
# Calling greet() with args: ('Mohammad',), kwargs: {}
# greet() returned: Hi, Mohammad!

# -----------------------------------------
# 🔹 Python open() Function
# -----------------------------------------

# Syntax:
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True)

# Common parameters:
# file     → The path to the file you want to open.
# mode     → Defines how the file is opened.
# encoding → Specifies text encoding (like 'utf-8') when working with text files.

# Common modes:
# 'r'  → Read (default). File must exist.
# 'w'  → Write. Creates a new file or overwrites existing one.
# 'a'  → Append. Adds content to the end of the file.
# 'x'  → Create. Fails if file already exists.
# 'r+' → Read and write (must exist).
# 'w+' → Write and read (overwrite).
# 'a+' → Append and read.

# -----------------------------------------
# ✅ Example 1: Reading a file
# -----------------------------------------

# Suppose we have a file: "example.txt" containing:
# Hello World!

file = open("example.txt", "r", encoding="utf-8")
content = file.read()   # Reads the entire file as a string
print(content)          # 🔹 Output: Hello World!
file.close()            # Always close the file when done


# -----------------------------------------
# ✅ Example 2: Writing to a file
# -----------------------------------------

file = open("output.txt", "w", encoding="utf-8")
file.write("This is a new line of text.")
file.close()

# If you open the file in 'w' mode again, it will overwrite the content.


# -----------------------------------------
# ✅ Example 3: Appending to a file
# -----------------------------------------

file = open("output.txt", "a", encoding="utf-8")
file.write("\nThis text was appended.")
file.close()


# -----------------------------------------
# ✅ Example 4: Reading line by line
# -----------------------------------------

file = open("output.txt", "r", encoding="utf-8")

for line in file:
    print(line.strip())  # strip() removes newline characters

file.close()


# -----------------------------------------
# ✅ Example 5: Using `with` (recommended way)
# -----------------------------------------

# 'with' automatically closes the file when the block ends
with open("output.txt", "r", encoding="utf-8") as file:
    data = file.read()
    print(data)
# File is closed automatically here


# -----------------------------------------
# ✅ Example 6: Read methods
# -----------------------------------------

with open("output.txt", "r", encoding="utf-8") as file:
    print(file.read(10))      # Read first 10 characters
    print(file.readline())    # Read one line
    print(file.readlines())   # Read all lines into a list


# -----------------------------------------
# ✅ Example 7: Binary mode
# -----------------------------------------

# Use 'rb' or 'wb' for binary files (like images or videos)
with open("image.jpg", "rb") as img_file:
    data = img_file.read()
    print(len(data))  # number of bytes read

# -----------------------------------------
# 🔹 with open() — Context Manager for Files
# -----------------------------------------

# The 'with' statement automatically opens and closes the file.
# You don’t need to call file.close().
# This is the recommended, safe way to handle files in Python.

# Syntax:
# with open(filename, mode, encoding) as variable:
#     # work with the file

# -----------------------------------------
# ✅ Example 1: Reading a file
# -----------------------------------------

with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
# 🔹 File is automatically closed here

# Output (if example.txt contains "Hello World!"):
# Hello World!


# -----------------------------------------
# ✅ Example 2: Writing to a file
# -----------------------------------------

with open("output.txt", "w", encoding="utf-8") as file:
    file.write("This file was created using with open().")

# 🔹 Automatically closed — no need for file.close()


# -----------------------------------------
# ✅ Example 3: Appending to a file
# -----------------------------------------

with open("output.txt", "a", encoding="utf-8") as file:
    file.write("\nNew line added at the end.")

# 🔹 'a' means "append" → keeps old data and adds new text


# -----------------------------------------
# ✅ Example 4: Reading line by line
# -----------------------------------------

with open("output.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())  # strip() removes newline characters

# 🔹 Output:
# This file was created using with open().
# New line added at the end.


# -----------------------------------------
# ✅ Example 5: Reading all lines into a list
# -----------------------------------------

with open("output.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines)
# 🔹 Output: ['This file was created using with open().\n', 'New line added at the end.']


# -----------------------------------------
# ✅ Example 6: Using multiple context managers
# -----------------------------------------

# You can open multiple files at once using commas
with open("file1.txt", "r", encoding="utf-8") as f1, open("file2.txt", "w", encoding="utf-8") as f2:
    data = f1.read()
    f2.write(data.upper())

# 🔹 Reads from file1.txt and writes uppercase version to file2.txt


# -----------------------------------------
# ✅ Example 7: Handling errors safely
# -----------------------------------------

try:
    with open("not_found.txt", "r", encoding="utf-8") as file:
        data = file.read()
except FileNotFoundError:
    print("⚠️ File not found!")


# -----------------------------------------
# 🔹 Python Requests Module
# -----------------------------------------
# You can install it (if not already):
# pip install requests

import requests

# -----------------------------------------
# ✅ 1. Simple GET request
# -----------------------------------------

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)  # 200 → OK
print(response.text)         # Returns raw text
print(response.json())       # Converts JSON response to a Python dict

# Output example:
# 200
# {"userId": 1, "id": 1, "title": "...", "body": "..."}


# -----------------------------------------
# ✅ 2. Sending Query Parameters
# -----------------------------------------

params = {"userId": 1}
response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)
print(response.url)  # Full URL with query → https://.../posts?userId=1
print(response.json())  # List of posts for userId=1


# -----------------------------------------
# ✅ 3. Sending a POST request (Create data)
# -----------------------------------------

data = {"title": "New Post", "body": "Content here", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
print(response.status_code)  # 201 → Created
print(response.json())       # Returns the created post


# -----------------------------------------
# ✅ 4. PUT request (Update data)
# -----------------------------------------

update_data = {"title": "Updated Title"}
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=update_data)
print(response.status_code)  # 200 → OK
print(response.json())


# -----------------------------------------
# ✅ 5. DELETE request
# -----------------------------------------

response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)  # 200 or 204 → Deleted


# -----------------------------------------
# ✅ 6. Custom Headers
# -----------------------------------------

headers = {"Authorization": "Bearer your_token_here"}
response = requests.get("https://jsonplaceholder.typicode.com/users", headers=headers)
print(response.status_code)


# -----------------------------------------
# ✅ 7. Timeout
# -----------------------------------------

try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=5)
    print(response.status_code)
except requests.Timeout:
    print("⚠️ Request timed out!")


# -----------------------------------------
# ✅ 8. Error Handling (Best Practice)
# -----------------------------------------

try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    response.raise_for_status()  # Raises an error for bad responses (4xx/5xx)
    print(response.json())
except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}")
except requests.exceptions.RequestException as err:
    print(f"Other Error: {err}")
