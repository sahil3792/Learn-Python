#WAP using to remove the duplicate elements in an array

import numpy
Size = int(input("Enter Size of Array :- "))
Array=[]

def RemoveDuplicate(Array):
    i=0
    for i in range(0,len(Array)):
        print("i iteration:- ",i)
        if i > len(Array):
            break 
        for j in range(i+1,len(Array)):
            print("J iteration:- ",j)
            if j < len(Array):
                if len(Array)>1:
                        
                    while Array[i]==Array[j]:
                        
                        Array.pop(j)
                        print("pop")
                        print("after popping j value = ",j)
                        print(len(Array))
                        print(Array)
                    
        #     print("J iteration:- ",j)
        #     if j < len(Array):
        #         if Array[i] == Array[j]:
        #             Array.pop(j)

            print(Array)
        
        

    print(Array)


    

for x in range(Size):
    Array.append(int(input("Enter number to add in Array:- ")))

RemoveDuplicate(Array)


#Output
# Enter Size of Array :- 10
# Enter number to add in Array:- 8
# Enter number to add in Array:- 6
# Enter number to add in Array:- 3
# Enter number to add in Array:- 2
# Enter number to add in Array:- 8
# Enter number to add in Array:- 3
# Enter number to add in Array:- 6
# Enter number to add in Array:- 8
# Enter number to add in Array:- 1
# Enter number to add in Array:- 6
# i iteration:-  0
# J iteration:-  1
# [8, 6, 3, 2, 8, 3, 6, 8, 1, 6]
# J iteration:-  2
# [8, 6, 3, 2, 8, 3, 6, 8, 1, 6]
# J iteration:-  3
# [8, 6, 3, 2, 8, 3, 6, 8, 1, 6]
# J iteration:-  4
# [8, 6, 3, 2, 3, 6, 8, 1, 6]
# J iteration:-  5
# [8, 6, 3, 2, 3, 6, 8, 1, 6]
# J iteration:-  6
# [8, 6, 3, 2, 3, 6, 1, 6]
# J iteration:-  7
# [8, 6, 3, 2, 3, 6, 1, 6]
# J iteration:-  8
# [8, 6, 3, 2, 3, 6, 1, 6]
# J iteration:-  9
# [8, 6, 3, 2, 3, 6, 1, 6]
# i iteration:-  1
# J iteration:-  2
# [8, 6, 3, 2, 3, 6, 1, 6]
# J iteration:-  3
# [8, 6, 3, 2, 3, 6, 1, 6]
# J iteration:-  4
# [8, 6, 3, 2, 3, 6, 1, 6]
# J iteration:-  5
# [8, 6, 3, 2, 3, 1, 6]
# J iteration:-  6
# [8, 6, 3, 2, 3, 1]
# J iteration:-  7
# [8, 6, 3, 2, 3, 1]
# i iteration:-  2
# J iteration:-  3
# [8, 6, 3, 2, 3, 1]
# J iteration:-  4
# [8, 6, 3, 2, 1]
# J iteration:-  5
# [8, 6, 3, 2, 1]
# i iteration:-  3
# J iteration:-  4
# [8, 6, 3, 2, 1]
# i iteration:-  4
# i iteration:-  5
# i iteration:-  6
# [8, 6, 3, 2, 1]


