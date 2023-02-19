class Time:
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
    def __add__(self, other):
        return self.__hour+other.__hour,self.__minute+other.__minute,self.__second+other.__second
t1=Time(7,35,45)
t2=Time(1,20,60)
print("The time after adding:",t1+t2)