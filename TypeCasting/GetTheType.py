def getTheFunction(variable):
    print(type(variable)) #this will print all values as string
    # type casting the variable and assigning then to a new variable
    stringvalue = str(variable)
    print("this will print string value",type(stringvalue))
    floatvalue = float(variable)
    print("this will print float value", type(floatvalue))


val = input("ENter a value:- ")
getTheFunction(val)