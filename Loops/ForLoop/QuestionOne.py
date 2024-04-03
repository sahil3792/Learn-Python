#write a program to print idd number 

number = int(input("Enter a Number:- "))
if (number%2)==0:
    number+=1

for number in range(number,10,2):
    print(number)
