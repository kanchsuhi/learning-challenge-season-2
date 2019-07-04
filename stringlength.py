#program to that calculates the string length and displays the length of the string until the user enters 'quit':
i=1
while(i>0):
    a=input("enter the string:")
    if(a!="quit"):
        print(len(a))
    else:
        break;
i=i+1

