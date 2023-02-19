class Rectangle:
    def __init__(self,length,width):
        self.__length=length
        self.__width=width
    def __lt__(self, other):
        return (self.__length*self.__width)<(other.__length*other.__width)
a1=Rectangle(10,50)
a2=Rectangle(6,2)
if a1<a2:
    print("Area2 is greater")
else:
    print("Area1 is greater")