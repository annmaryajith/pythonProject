#colorlist1=input("enter list:")
#colorlist2=input("enter list2:")
#list1=colorlist1.split(",")
#list2=colorlist2.split(",")
#print(list1)
#print(list2)
#l=set(list1).difference(list2)
#print(l)

line=input("enter line of words:")
dict={}
list=line.split()
for word in list:
    if word in dict:
        dict[word]+=1
    else:
        dict[word]=1
for x,y in dict.items():
    print(x,y)