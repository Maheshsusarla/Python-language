# #Data Types

# In programming, data type is an important concept.

# Variables can store data of different types, and different types can do different things.

# Python has the following data types built-in by default, in these categories:


# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

#int
a=23
print(a,type(a))

#float
b=2.3
print(b,type(b))

#complex
com=2+5j
print(com,type(com))

#string 
c='mahesh'
d="mahi"
print(c,type(c))
print(d,type(d))


#bool
e=True
f=False
print(e,type(e))
print(f,type(f))

#list
g=[1,2,3,4,5]
print(g,type(g))


#tuple
tup=(1,2,3,4,5)
print(tup,type(tup))

#dict
h={
    "name":"mahesh",
    age:23
}
print(h,type(h))



#set
s={1,2,3,4,5}
print(s,type(s))


#range
x=range(5)
print(x,type(x))