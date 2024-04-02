#Write a program to check whether a number is equal greater or smaller

A = int(input("Enter A Number"))
B = int(input("Enter A Number"))

if A>B:
    print(A,"is Greater than",B)
elif A==B:
    print(A,"is Equal to",B)
else:
    print(A,"is Smaller then",B)