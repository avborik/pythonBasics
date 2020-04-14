# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
# print(1)
print('Welcome to Python course')

# x = 1              #int
# y = 2.5            #float
# name = 'Boris'     #String
# is_cool = True     #boolean

#multiple assignment
x, y, name, is_cool = (1, 2.5, 'Boris', True)

print(x,y,name,is_cool) 

#Basic math

a = x + y

print(a)

#Check the variables, types

# print(type(a))
print(type(x))

#Casting
x = str(x)
print(type(x))
