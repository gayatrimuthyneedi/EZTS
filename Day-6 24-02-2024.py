#problem-1
'''class classn:
    def __init__(self,n):
        self.n=n
    def isprime(self()):
        c=0
'''

 #problem=2
'''class check:
    def __init__(self,n):
      self.n=n
    def ispalandrome(self):
        if self.n==self.n[::-1]:
            print("yes")
        else:
            print("no")
obj1=check("hello")
obj2=check("sas")
obj1.ispalandrome()
obj2.ispalandrome()
'''

#problem-3

'''class total:
    def __init__(self,n):
        self.n=n
    def isprime(self):
        c=0
        for i in range(2,self.n):
            if self.n%2==0:
                c=c+1
        if c==0:
            print("prime")
        else:
            print("not a prime")
    def ispalindrome(self):
        if str(self.n)==str(self.n[::-1]):
            print("yes")
        else:
            print("no")
obj1=total(22)
obj2=total(24)
obj1.isprime()
obj2.isprime()
obj1.ispalindrome() 
obj2.ispalindrome()
'''

#problem=4
#access specifers example 
#public 
'''class car:
    maxspeed=0
    name=""
    def __init__(self):
        self.maxspeed=200
        self.name="supercar"
    def drive(self):
        print(self.maxspeed)
car1=car()
car1.drive()
car1.maxspeed=10
car1.drive()'''
#problem-5
#access specifiers 
#private
'''class car:
    __maxspeed=0
    __name=""
    def __init__(self):
        self.__maxspeed=200
        self.__name="supercar"
    def drive(self):
        print(self.__maxspeed)
car1=car()
car1.drive()
car1.__maxspeed=10
car1.drive()'''
#inheritance (using super class)
'''class parent:
    def __init__(self):
        print("parent method")
class child(parent):
    def __init__(self):
        super().__init__()
        print("child method")
c=child() '''
#inheritance (without using super class)
''''class parent:
    def __init__(self):
        print("parent method")
class child(parent):
    def __init__(self):
        print("child method")
c=child()'''
#problem using single inheritance ans super class 
'''class dob:
    def __init__(self,date,month,year):
        self.date=date
        self.month=month
        self.year=year
    def display1(self):
        d={ 1:"jan",2:"feb",3:"march",4:"april",5:"may",6:"june",7:"july",8:"aug",9:"sep",10:"oct",11:"nov",12:"dec"}
        print(self.date)
        print(d[self.month])
        print(self.year)
class details(dob):
    def __init__(self,name,age,date,month,year):
        self.name=name
        self.age=age
        self.date=date
        self.month=month
        self.year=year
        super().__init__(self.date,self.month,self.year)
    def display(self):
        print(self.name)
        print(self.age)
        print(self.date)
        print(self.month)
        print(self.year)
p=details("abc",21,24,1,2001)
p.display()
p.display1()'''

#multilvel inheritance 
'''class parent:
    def func1(self):
        print("this is function1")
class child(parent):
    def func2(self):
        print("this is funtion2")
class child2(child):
    def func3(self):
        print("this is function3")
ob=child2()
ob.func1()
ob.func2()
ob.func3()'''

# abstraction problem
'''from abc import ABC,abstractmethod
class shape(ABC):
    def  display(self):
        pass
class rectangle(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area1(self):
        print(self.l*self.b)
class square(shape):
    def __init__(self,s):
        self.s=s
    def area2(self):
        print(self.s*self.s)
ob1=rectangle(2,4)
ob2=square(2,2)
ob2.area2()'''
'''from abc import ABC,abstractmethod
class a(ABc):
    @abstractmethod
'''

#exception handling 
'''try:
    a=int(input())
    x=a//0
except:
    print("error occured")
else:
    print(x)
finally:
    print("hi")'''
#approach-2
try:
    a=int(input())
    x=a//2
except:
    print("error occured")
except Exception as e:
    print(e)
else:
    print(x)
finally:
    print("hi")