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
