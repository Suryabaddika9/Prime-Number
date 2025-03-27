a=int(input())
b=int(input())

for i in range(a,b+1):
    factors = 1
    for j in range(2,i):
        if i%j==0:
            factors+=1
    if factors==1:
        print(i)
