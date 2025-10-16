num_1 = 5 # integer
num_2 = 5.5 # float
num_3 = 5j # complex
lastName = "babakhani"
# Priority of math operations: 1.() 2.** 3.*/ 4.+-
print(type(num_1)) #integer
division = 8 / 4 # answer always will be float => 2.0
Remainder = 9 % 2 # Remainder of division => 1
# Types of variables: 1.integer 2.str 3.boolean 4.list 5.dic 6.none
dicExample = { "name": "mohammad", "age": 24 }
print("my name is 'mohammad'") # To write inside double quotes, single quotes must be used.
print("my name is \"mohammad\"") # escape chars
print("firstNamr \n lastName") # new Line
"mohammad" + " " + "babakhani" # str concat
f"mohammad {lastName}" # str interpolation
# In string interpolation, when a mathematical operation is performed, the Python kernel converts the number to a string.
# 1.int() 2.float() 3.str()
input() # Receives input from the user. 
# The input it receives is a string.
round(5.555, 2) # Rounding up
# ----------------------------------------------------------------------
rank = int(input())
if(rank == 1):
    print("Gold")
elif(rank == 2):
    print("Silver")
elif(rank == 3):
    print("Bronze")
else:
    print("none")
# ----------------------------------------------------------------------
print("Gold")if(rank == 1) else print("none") #else-if short hand
# the == operator => values are equal
# the is operator => point to the same object
obj_1 = ["A"]
obj_2 = list(obj_1)
obj_1 == obj_2 # true
obj_1 is obj_2 # false
# ----------------------------------------------------------------------
# comparison operators 1.== 2.!= 3.> 4.< 5.>= 6.<=
# logical operators 1.and 2.or 3.not
# import random print(random.randint(0,3))
# lower()
# for loop: for item in collection: pass
# collection: 1.list of numbers 2. list of chars in a string 3. range(1,5) etc
# range(start, finish, step)
print(list(range(1, 10))) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for item in range(1,5):
    print('*' * item)

for item in range(1,3):
    if (item % 2 == 1):
        for star in range(1,3):
            print('*' * star)
    else:
        for star in range(3,0,-1):
            print('*' * star)

for item in range(1,5):
    for star in range(item):
        print('*', end='')
    print()
# ----------------------------------------------------------------------
num = 1
while num <= 10:
    print(num)
    num += 1

for num in range(1,5):
    stars = ''
    for star in range(1, num + 1):
        stars += '*'
    print(stars)
# ----------------------------------------------------------------------
list_1 = ['python', 'react', 'javascript']
len(list_1) # length of list
isExistPython = 'python' in list_1 # is child exists in list
for item in list_1:
    print(item)

index = 0
while index in list_1:
    item = list_1[index]
    print(item)
    index += 1
# ----------------------------------------------------------------------
list_1 = ['python', 'react']
list_2 = ['vue', 'nuxt']
list_1.append('JS') # add one item to end of list
list_1.extend(list_2) # add list's child to another list
list_1.insert(1,'next') # add based on index
# ----------------------------------------------------------------------
# list_1.clear() # remove whole list
list_1.pop() # remove and return last item
list_1.pop(0) # remove and return item by index
list_1.remove('vue') # remove item by str
# ----------------------------------------------------------------------
list_1.index('JS') # finding index
list_1.count('python') # تعداد یک ایتم 
list_1.reverse()
list_1.sort() # Sort the list in ascending order and return None.
", ".join(list_1) # Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
print(list_1)
# ----------------------------------------------------------------------
list_1 = [1,2,3,4,5]
# list_1[start:end:step]
# list_1[1:3] # [1, 2]
# list_1[1:5:2] # [2, 4]
# list_1[2:] # [3, 4, 5]
# list_1[:3] # [1, 2]
# list_1[::2] # [2, 4]
list_2 = list_1[:] # یک کپی از لیست ایجاد میکند
print(list_1 is list_2) # وقتی یک کپی از لیست گرفته میشود با خود لیبست برابر است (==) اما به یک نقطه از حافظه اشاره نمیکند
# comprehension list
list_2 = [num * 2 for num in list_1]
# ----------------------------------------------------------------------
dict_1 = dict(name = 'mohammad') # {"name": "mohammad"}
dict_2 = {"name": "A", "age": 24, "isOnline": True}
print([value for value in dict_2.values()]) # ['A', 24, True]
print([key for key in dict_2.keys()]) # ['name', 'age', 'isOnline']
print([item for item in dict_2.items()]) # [('name', 'A'), ('age', 24), ('isOnline', True)]
print("name" in dict_1) # check if the key exist in dictionary
print("mohammad" in dict_1.values()) # check if the value exist in dictionary
# ----------------------------------------------------------------------
# dictionary methods
dict_1.clear() # remove all item inside dictionary
dict_1.copy()
dict_3 = {}.fromkeys(["name"], "unknown") # => {"name": "unknwon"} using it for generating default values
dict_1.get("name") # => dict["name"] خروجی get به صورت None هست و پروژه را دچار مشکل نمیکند 
dict_1.pop("name") # remove and return key and value from dictionary
dict_1.popitem() # remove last key and value from dictionary
dict_1.update({"name": "Liza"}) # add dictionary
# comprehension dictionary
dict_4 = dict(first = 1, second = 2, third = 3)
squaredNumbers = {key: value ** value for key, value in dict_4.items()}
{num : ("even" if num % 2 == 0 else "odd") for num in [1, 2, 3, 4, 5]}
# ----------------------------------------------------------------------
# tuple
tuple_1 = (1, 2, 3) # immutable list
print(tuple_1[0])
print(3 in tuple_1)
# why we use tuple??? 1. faster than list 2.use less memory 3.immutable list4
print(tuple([1, 2, 3]))

location = {
    (35.67, 45.78): "Tehran"
}
print(location[(35.67, 45.78)])
tuple_1.count(1)
tuple_1.index(5)
# slicing in list is available in tuple
# ----------------------------------------------------------------------
set_1 = {1, 2, 3, 4} # تکرار در ست معنا ندارد
# بر اساس ایندکس به ایتم ها دسترسی ندارم
# هیچ ترتیب خاصی برای ست ها وجود ندارد
# we can use loops to hava access to the items in set 
courses = ['PY', 'JS']
courses_set = set(courses)
list((1, 2, 3)) # [1,2,3]
numbers_set = {1,2,3}
numbers_set.add(5) # اگر عدد تکراری باشد به ست اضافه نمیشود
numbers_set.remove(2)
numbers_set.discard(5) # تنها تفاوت discard و remove این است که discard زمانی که ایتم مورد نظر در ست نباشد خطا نمیدهد
copyNumbers = numbers_set.copy()
numbers_set.clear()
PY = ["mohammad", "reza"]
JS = ["reza", "nader"]
print(PY | JS) # ["mohammad", "nader"] اجتماع
print(PY & JS) # ["mohammad", "nader"] اشتراک
# ----------------------------------------------------------------------
for item in ["PY", "JS"]:
    print(item, end="-") # PY-JS-
    print(item, sep="-") # PY-JS
# ----------------------------------------------------------------------
response_code = 201
match response_code:
    case 200:
        print("OK")
    case 201:
        print("fuck")
# ----------------------------------------------------------------------
def printShit(shit):
    print(shit)

def add (number):
    return number + 6
# به متغیرهایی که برای ورودی فانکشن ها تعریف میشن => پارامتر
# مقادیری که برای ورودی فانکشن در نطر میگیریم => آرگومان

def hi(word = "hi"): # default value
    print(word)
hi(word= "bitch") # مشخص مقدار ورودی

# *args
def plus(*args):
    total = 0
    for arg in args:
        total += arg
    print(total)
plus(1,2,3,4,4,5)

# ** kwargs
def kwargs(**kwargs):
    print(kwargs)

kwargs(name="mohammad") # {'name': 'mohammad'}

def plus (num1) : print(num1)
# anonymous function 
short_version = lambda num : print(num) # مقدار خروجی را به صورت پیشفرض return میکند
short_version(5)
# ----------------------------------------------------------------------
list_1 = [1,2,3,4]
print(list(map(lambda num: num * num, list_1)))
print(list(filter(lambda num: num % 2 == 0, list_1)))
all() # یک لیست به عنوان ورودی میگیرد و truthy و falthy رو بررسی مبکند اگر تمام ایتم ها درست بود true برمی گردونه
any() # اگر تنها یکی از ایتم ها درست بود true برمیگردونه
# ----------------------------------------------------------------------
list_1 = [1,2,3,4]
list_2 = [5,6,7,8]
print(list(zip(list_1,list_2))) # [(1, 5), (2, 6), (3, 7), (4, 8)]
print(dict(zip(list_1,list_2))) # {1: 5, 2: 6, 3: 7, 4: 8}
# وقتی میای literate میکنی ایتم های درون زیپ ابجکت رو دیگه ایتم های اون از بین میرن و برای بار دوم نمیشه اون داخل لیست نوشت
print(list(zip(*[(1, 5), (2, 6), (3, 7), (4, 8)]))) # [(1, 2, 3, 4), (5, 6, 7, 8)]
# ----------------------------------------------------------------------
# syntaz error
# name error
# type error
# value error
# key error
# attribute error
raise IndexError('index error')

try:
    pass
except:
    pass
else:
    pass
finally:
    pass