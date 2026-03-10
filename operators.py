# # Python Operators

# # Operators are used to perform operations on variables and values.

# Python divides the operators in the following groups:

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# Arithmetic Operators:
# Arithmetic operators are used with numeric values to perform common mathematical operations:

# x = 15
# y = 4

# print(x + y) Addition
# print(x - y) Subtraction
# print(x * y) Multiplication
# print(x / y) Division
# print(x % y) Modulus 
# print(x ** y) Exponentiation
# print(x // y) Floor division Floor division (returns an integer)

#Assignment operators
#Assignment operators are used to assign values to variables:
x = 10

x += 5
print(x)   

x -= 3
print(x)   

x *= 2
print(x)   

x /= 4
print(x)   



# Comparison Operators
# Comparison operators are used to compare two values:
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)




# Logical Operators
# Logical operators are used to combine conditional statements:
ExampleGet your own Python Server
#and 
x = 5
print(x > 0 and x < 10)

#or
x = 5
print(x < 5 or x > 10)

#not 
x = 5
print(not(x > 3 and x < 10))

#Identity Operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
#is 
The is operator returns True if both variables point to the same object:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)
#is not
The is not operator returns True if both variables do not point to the same object:

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)
Difference Between is and ==
is - Checks if both variables point to the same object in memory
== - Checks if the values of both variables are equal


Membership Operators
Membership operators are used to test if a sequence is presented in an object:
#in 
Check if "banana" is present in a list:

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)

#not in 
Check if "pineapple" is NOT present in a list:

fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)


#ist of Bitwise Operators

AND → &
OR → |
XOR → ^
NOT → ~
Left Shift → <<
Right Shift → >>
a = 10   # 1010 in binary
b = 4    # 0100 in binary

print("a & b =", a & b)   # AND
print("a | b =", a | b)   # OR
print("a ^ b =", a ^ b)   # XOR
print("~a =", ~a)         # NOT
print("a << 2 =", a << 2) # Left Shift
print("a >> 2 =", a >> 2) # Right Shift