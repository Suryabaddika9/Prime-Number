a=int(input())
b=int(input())

x=[]

for i in range(a):
    y=[]
    for j in range(b):
        y=y+[i+j]
    x.append(y)
print(x)