
list_a=[]
for k in range(int(input("Enter number of Values to be Entered: "))):
    name = input("Name of Student: ")
    score = float(input("Marks Obtained: "))
    list_a.append([name,score])
print(list_a)
values=[]
for list_b in list_a:
    values=values+[list_b[1]]
print(sorted(values))
values=sorted(values)
values=sorted(values)
op=[]
for x in list_a:
    if values[1]==x[1]:
        op=op+[x[0]]
print(sorted(op))
for l in sorted(op):
    print(l)
