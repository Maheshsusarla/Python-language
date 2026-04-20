# Lists are used to store multiple items in a single variable.

# Lists are one of 4 built-in data types in Python used to store collections of data,
#  the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Lists are created using square brackets: []
# is a order 
# immutable -you can change add remove everything

# thislist = ["apple", "banana", "cherry"]
# print(thislist)

my_list=[1,2,3,4,5,6,7,8,9,5,4,3,4,5]

# print(my_list[0])
#slicing
# print(my_list[0:5])
# print(my_list[:8])

#reverse sclicing
# print(my_list[::-1])

#start :End :step
# print(my_list[2:8:5]) #after 2 index it will count


#updating the list
# my_list[7]="Mahesh"
# my_list[-1]="mahi"

# print(my_list[7])

# last index
# print(my_list[-1])

#delect item in list specific index use del keyword
# del my_list[0]
# print(my_list)


# mylis=[1,2,3,4,5]
# mylis.remove(5) -remove specific item in list
# print(mylis)

#use matrix
# mat=[
#     [1,2,3], #this is a 0 index in side index will be valuesnlike 1,2,3
#     [4,5,6] #and its is a 1 indes  also same

# ]
# print(mat[0][0]) 
# print(mat[1][0])

#mat inside matrix and inside is there
# mats=[
#     [
#         [1,2,3],
#         [4,5,6]
#     ],
#     [
#         [7,8,9]
#     ]
# ]
# print(mats)
# print(mats[0][0]) 
# print(mats[0][1])

#append method to add an last index
hi=[1,2,3,4,5]
# hi.append("Mahesh")
# print(hi)

#index it returns the index value
c=lis.index(9)
print(c)

#to add an multiple elements from an iterable to the end of exsting list
# hi.extend([6,7,8])
# print(hi)

#to add an single element to a list at the specific ,user define position
# hi.insert(0,"mahesh")
# print(hi)

#to delete the first occurrence of a specified value from a list
# hi.remove(2)
# print(hi)

#remove last element by default - and you can delete a speicific index also
# hi.pop() -remove last element
# hi.pop(2)
# print(hi)

#to reorder the elements of a list specific sequence ,ascending by default
lis=[9,7,6,5,4,3,2,1]
# print(lis)
# lis.sort()
# print(lis)

#to create a new,independent list from an existing one.allowing to the new list without affecting the orginal
# lis=[1,2,3]
# lis.copy()
# print(lis)

# lis.reverse()
# print(lis)

#count -it returns the occurence of the list
# lis.count(1)
# print(lis)

# lis=[1,2,3,4,5]
# # for i in lis:
# #     print(i)


# i=0
# while i<len(lis):
#     print(lis[i])
#     i+=1

# tex="mahesh is a developer"
# res="developer" in tex
# res1="hi" in tex
# print(res)
# print(res1)
