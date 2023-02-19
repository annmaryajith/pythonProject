n=int(input("Enter a number: "))
sum=0
for i in range(3):
    i=int(pow(n,i+1))
    print(i)
    sum=sum+i
print("Sum = ",sum)