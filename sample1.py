#def factor(num):
#   print("factors")
#   for i in range(1,num+1):
#       if num%i==0:
#           print(i)
#factor(10)

#str=input("enter a string:")
#if str.endswith('ing'):
#   str=str.strip('ing')
#   str+='ly'
#elif len(str)>=3:
#   str+='ing'
#print(str)

x=int(input("enter 1st no:"))
y=int(input("enter 2nd no:"))
gcd=1
for i in range(1,max(x,y)):
    if x%i==0 and y%i==0:
        gcd=i
print("gcd=",gcd)
