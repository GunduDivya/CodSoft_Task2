import sys

print("\t\t\t\t\t\t\t\t\t basic calculator")
print("""\t\t1.Addition
        2.Subtraction
        3.Multiplication
        4.Division
        5.Floor Division
        6.Modulo Division
        7.Exponentiation
        8.Exit
        """)
a=int(input("enter first value:"))
b=int(input("enter second value:"))
while(True):
    choose=int(input("enter which operator you want:"))
    if choose==1:
        print('addition')
        c=a+b
        print(" {} +{}={}".format(a,b,c))
    elif choose==2:
        c=a-b
        print("subtraction",c)
    elif choose==3:
        print("Multiplication")
        c=a*b
        print("{} *{}={}".format(a,b,c))
    elif choose==4:
        print("Division")
        c=a/b
        print("{}/{}={}".format(a,b,c))
    elif choose==5:
        print("floor Division")
        c=a//b
        print("{}//{}={}".format(a,b,c))
    elif choose==6:
        print("Modulo Division")
        c=a%b
        print("{} %{}={}".format(a,b,c))
    elif choose==7:
        print("Exponentiation")
        c=a*b
    elif choose==8:
        sys.exit()


    else:
        print("thanks for using this ")