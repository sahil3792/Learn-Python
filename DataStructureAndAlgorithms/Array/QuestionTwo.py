# Write a Python program to insert a newly created item before the second element in an existing array.
# Sample Output:
# Original array: array('i', [1, 3, 5, 7, 9])
# Insert new value 4 before 3:
# New array: array('i', [1, 4, 3, 5, 7, 9])
Size = int(input("Define Size of array:- "))
Array = []

def InsertElement(Array,NewElement,BeforeElement):
    print(Array)

    for x in range(len(Array)):
        print(x)
        if Array[x] == BeforeElement:
            print("found value")
            for y in range(x,len(Array)-x):
                print("x =", x)
                print("length", len(Array)-x)
                print(Array)
                print(y)
                NewVar = Array[y]
                print("new var",NewVar)
                Array.insert(y+1,NewVar)
                print(Array)
                Array.insert(x,NewElement)
                print(Array)
                
                break
            
            break
for x in range(Size):
    Array.append(int(input("Add Elemet to Array :- ")))

NewElement = int(input("Enter New Element:- "))
print(Array)
BeforeElement = int(input("Insert new value before :- "))

InsertElement(Array,NewElement,BeforeElement)


