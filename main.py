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