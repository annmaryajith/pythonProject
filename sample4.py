l=int(input("enter no:"))
print("enter names:")
list=[]
count=0
for i in range(0,l):
    e=input()
    list.append(e)
print(list)
for i in list:
    for j in list:
        if j=='a':
            count=count+1
print("a occurs",count,"times")