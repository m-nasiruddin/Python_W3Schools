#!/bin/python3
# creating variable
a = 5
print(a)
b = "Salam"
print(b)

# legal variable names
# rule-1: a varible can only containt alphaneumeric characters (a-z, A-Z) and underscores (_)
my_var = 0  # rule-2: a variable must start with a letter or an underscore
print(my_var)
_my_var = 1  # as above
print(_my_var)
myvar = 2  # rule-3: variables are case-sensitive (myvar, myVar and MYVAR are three different variables)
print(myvar)
myVar = 3  # as above
print(myVar)
MYVAR = 4  # as above
print(MYVAR)
e = 5  # e and E are two different variables with two different types
print(e)
E = "Awal"  # as above
print(E)
myvar2 = 6  # satiesfies rule-1, 2 and 3
print(myvar2)
v = 7  # remember: a variable name can be short or more descriptive
print(v)
myVar = 8  # as above
print(myVar)
# note: all above variable names are different

# illegal variable names (will produce an error in the result)
# my var = 9  # cannot contain any space (rule-1)
# my.var = 10  # as above
# my-var = 11  # as above
# my@var = 12  # as above
# 2myvar = 13  # cannot start with a number (rule-2)
# int = 14  # rule-4: must not contain any key/reserve words (str, def, return, etc.)

# multiword variable names
# Pascal case
MyVariableName = "Salam"  # each word starts with a capital letter
# Camel case
myVariableName = "Rafiq"  # each word, except the first, starts with a capital letter
# Snake case
my_variable_name = "Barkat"  # each word is seperated by an underscore character

# single/double quotes in String variable
d = "Jabbar"
print(d)
d = 'Shafiur'  # double quotes are the same as single quote
print(d)

# value assignment (multiple values)
# assign values to multiple variables
i, j, k = 4, "Salam", "A"
print(i)
print(j)
print(k)

# assign the same value to multiple variables
l = m = n = 5
print(l, m, n)

# unpack a collection
martyrs = ["Salam", "Rafiq", "Barkat"]
o, p, q = martyrs
print(o, p, q)

# variable data type can be changed even after they have been set
c = 4  # x is of type int
c = "Rafiq"  # x is now of type str
print(c)

# variable data casting
x = str(3)
print(x)
y = int (3)
print(y)
z = float(3)
print(z)

# get the data type
m = 15
print(type(m))
n = 15.0
print(type(n))
o = "Barkat"
print(type(o))

# output variables
p = "awsome"
print("Python is " + p)  # to combine both text and variable
q = "Python is "
r = 'awsome'
s = q + r  # to concatenate two string
print(s)
u = 5
v = 10
print(u + v)  # works as a mathematical operator
w = 3
x = "Three"
# print(w + x)  # cannot combine a string and a number
print(w, "=", x)
