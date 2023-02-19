
list = ["Apple", "Orange", "Banana", "Strawberry", "Mango"]
file = open("list.txt", "w")
for element in list:
    file.write(element + "\n")
file.close()