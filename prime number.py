#program to find a number is either prime or not:
a=int(input("enter the number"))
if(a==1):
    print("the number is neither prime nor composite")
elif(a>2):
          for i in range (2,a):
             if(a%i==0):
                 print("the number is composite")
                 break;
          else:        
                print("the number is prime")
          
