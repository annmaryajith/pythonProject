f=open("demo.txt","r")
#f.write("\nnew content added")
#list=f.readlines()
#print("line by line......",list)

f1=open("odd.txt","w")
content=f.readlines()
for i in range(0,len(content)):
    if i%2!=0:
        f1.write(content[i])
    else:
        pass
f.close()
f1.close()
f=open("odd.txt","r")
c=f.read()
print("odd lines : ",c)
f.close()