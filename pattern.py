#program to generate a pattern:
for i in range(1,6):
    print()
    for j in range(i):
        print("*",end=" ")
for i in range(1,6):
    print()
    for j in range(5-i):
        print("*",end=" ")
