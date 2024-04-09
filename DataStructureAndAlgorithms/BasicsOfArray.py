import array as arr # importing Array module

#arr.array() #creation of array

#----- two ways of creating array-----

from array import *

#array()

#------How to define array 

#variable_name = array(typecode,[elements])


numbers = array('i',[10,20,30])
print("print the elements in array :- ",numbers)

print("print the elements at index 2:-" ,numbers[2])


#how to search through an array in python


print(numbers.index(20))



values =  array('i',[10,20,30,40,50,60,70,80,90])

print(values)

for x in range(len(values)):
    print(values[x])


#slice an array in python

print(values[1:3])