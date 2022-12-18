#n=int(input("Enter the limit: "))
#for i in range (1,n+1):
#   for j in range (1,i+1):
#       sqr=i*j
#       print(sqr,end=" ")
#   print()

#n=int(input("Enter the limit: "))
#for i in range(n):
#   for j in range(i):
#       print("*",end=" ")
#   print(' ')
#for i in range(n,0,-1):
#   for j in range(i):
#       print("*",end=" ")
#   print(' ')

n=int(input("enter the limit: "))
print("enter the words: ")
list=[]
for i in range(0,n):
    e=input()
    list.append(e)
def longest(list):
    return max(list,key=len)
print("longest=",longest(list))
print("length=",len(longest(list)))
print(list)