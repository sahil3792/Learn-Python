# WAP to give grade to student entered their marks

Name = input("Enter Your Name:-")
Percentage =int(input("Enter your Percentage"))

Stack=[Name, Percentage]

print(Stack)

if Percentage>35:
    if Percentage<=45:
        print(Name+" has Scored E Grade by",Percentage,"Percentagle")
    else:
        if Percentage<=60:
            print(Name+" has Scored D Grade by",Percentage,"Percentagle")
        else:
            if Percentage<=75:
                print(Name+" has Scored C Grade by",Percentage,"Percentagle")
            else:
                if Percentage<=90:
                    print(Name+" has Scored B Grade by",Percentage,"Percentagle")
                else:
                    if Percentage>90:
                        print(Name+" has Scored A Grade by",Percentage,"Percentagle")


else:
    if Percentage>25:
        print("Failed")
    else:
        print("LC")


#90>75>60>45>35