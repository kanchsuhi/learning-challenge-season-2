#write a program that determines whether a student is eligible for PG course or not .To eligible ,the student must have obtained more than 80% in X and XII exam,and 70% plus marks in graduation.If the student changes his streams (science,commerce,or arts),then deduct 5% from his graduation score
x=int(input("enter the X percent:"))
y=int(input("enter the XII percent:"))
z=int(input("enter the graduation marks:"))
a=input("did you changed your stream:")
if(x>80 and y>80):
    if(a=="yes"):
        z=z-5
        print(z)
        if(z>70):
            print("eligible")
        else:
            print("not eligible")
        



