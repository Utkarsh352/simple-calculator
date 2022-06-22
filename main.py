while True:
    print("hey! welcome enter any number to continue and q to quit")
    num1=input()
    if num1=="q":
        break
    else:
        print("Please enter a number")
        numA=float(input())
        print("what would you like to do with it\n1=>add\n2=>subtract\n3=>multiply\n4=>divide")
        operator=int(input())
        print("enter the 2nd number")
        numB=float(input())
        if operator==1:
            print(numA+numB)
        elif operator==2:
            print(numA-numB)
        elif operator==3:
            print(numA*numB)
        elif operator==4:
            print(numA/numB)
