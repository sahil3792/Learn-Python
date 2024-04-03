Num = int(input("Enter a Number:- "))

Final=0

for x in range(100):
    EndNumber = Num%10
    Num = int(Num/10)
    
    print(EndNumber)
    Final=Final+EndNumber
    print(Final)

    # print(Num)
    if Num==0:
        print()
        break
    
    