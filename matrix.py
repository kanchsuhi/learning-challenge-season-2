a=[]
b=[]
c=[]
i=0
j=0
n=int(input("enter the no.of.rows:"))
m=int(input("enter the no.of.columns:"))
r=int(input("enter the no.of.rows:"))
s=int(input("enter the no.of.columns:"))
for i in range (0,m):
    a.append([])
for i in range(0,n):
    for j in range(0,m):
        a[i].append(j)
        a[i][j]=0
for i in range(0,n):
    for j in range (0,m):
        a[i][j]=int(input("enter the number:"))
print("the matrix A is:",a)


for i in range (0,s):
    b.append([])
for i in range(0,r):
    for j in range(0,s):
        b[i].append(j)
        b[i][j]=0
for i in range(0,r):
    for j in range (0,s):
        b[i][j]=int(input("enter the number:"))
print("the matrix B is:",b)

for i in range (0,s):
    c.append([])
for i in range(0,r):
    for j in range(0,s):
        c[i].append(j)
        c[i][j]=0
for i in range(0,r):
    for j in range (0,s):
        c[i][j]=a[i][j]+b[i][j]
print("the additon of two matrix A abd B is:",c)

