# Q3. Write a program to print all even numbers that 
# falls between two number(exclusive both numbers) 
# entered from the user using while loop
Number1 = int(input("Enter a Number:- "))
Number2 = int(input("Enter a Number:- "))

while Number1<=Number2:
    if (Number1%2)==0:
        print(Number1)
        Number1+=2
    else:
        Number1+=1
        
