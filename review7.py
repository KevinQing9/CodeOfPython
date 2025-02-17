# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 21:19:15 2025

@author: qing
"""

class Dog:
    name="" #类的成员变量称为属性
    age=0
    def run(self):
        print("Dog is running")
    def eat(self):
        print("Dog is eating")

class User:
    username = ""
    mobile = ""
    address = ""
    def describe_user(self):
        print("user detail: username:%s mobile:%s address:%s"%(self.username,self.mobile,self.address))

user1 = User() #创建user1对象
user1.username="Kevin"
user1.mobile = "15311553355"
user1.address = "Forsyth road"
user2 = User() #创建user2对象
user2.username = "Kelly"
user2.mobile = "17211772211"
user2.address = "Anazac road"
user1.describe_user()
user2.describe_user()


import math
class Circle:
    def setradius(self,radius):
        self.radius = radius
    def showArea(self):
        area = self.radius**2*math.pi #可以直接调用self.radius获取成员变量的值
        print("circle's area=%.2f"%area)
circle = Circle()
circle.setradius(5)
circle.showArea()

class Student:
    count=0
    def addStudent(self,name,sex):
        self.name=name
        self.sex= sex
        Student.count+=1
    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age
stu1 = Student()
stu1.addStudent("Kevin", "Male")
stu2 = Student()
stu2.addStudent("Kelly","Female")
print(Student.count)
stu1.setAge(23)
print("stu1 name:%s sex:%s age:%d"%(stu1.name,stu1.sex,stu1.getAge()))

class Flight:
    '''def __init__(self): #无参构造方法
        self.startCity = "Beijing"
        self.destCity = "Shanghai"
        self.flyTime = "2019-09-10 18:28"
    def showFlight(self):
        print("startCity:%s destCity:%s flyTime:%s"%(self.startCity,self.destCity,self.flyTime))
flight1 = Flight()
flight1.showFlight()'''

    def __init__(self,startCity,destCity,flyTime): #有参构造方法
        self.startCity = startCity
        self.destCity = destCity
        self.flyTime = flyTime
    def __del__(self):
        print("invoke destrutor method")
    def showFlight(self):
        print("startCity:%s destCity:%s flyTime:%s"%(self.startCity,self.destCity,self.flyTime))
flight1 = Flight("Chengdu","Nanjing","2025-01-04 7:00")
flight1.showFlight()
flight2 = Flight("Chengdu","Sydney","2025-01-01 1:45")
flight2.showFlight()

class ClassInfo:
    number = 0
    @classmethod
    def addNum(cls,num):
        cls.number+=num
    @classmethod
    def getNum(cls):
        return cls.number
ClassInfo.number = 10
ClassInfo.addNum(20)
print("class number:%d"%ClassInfo.getNum())

class Person:
    country = "China"
    def getCountry():
        print("come from %s"% Person.country)
Person.getCountry()

'''class SchoolMember:
    def __init__(self,username,depart,sex):
        self.username = username
        self.depart = depart
        self.sex = sex
    def showInfo(self):
        print("username:%s department:%s sex:%s"%(self.username,self.depart,self.sex))
class Teacher(SchoolMember):
    def __init__(self,username,depart,sex,title):
        SchoolMember.__init__(self, username, depart, sex)
        self.title = title
    def showTitle(self):
        print("teacher's title:%s"%self.title)
class Student(SchoolMember):
    def __init__(self,username,depart,sex,major):
        SchoolMember.__init__(self, username, depart, sex)
        self.major = major
    def showMajor(self):
        print("student's major:%s"%self.major)
student1 = Student("Kevin","College of AI", "male","Blockchain engineering")
student1.showMajor()
student1.showInfo()
teacher1 = Teacher("Wu", "College of AI","male","Dean")
teacher1.showTitle()
teacher1.showInfo()'''

class SchoolMember:
    def __init__(self,username,depart,sex):
        self.username = username
        self.depart = depart
        self.sex = sex
    def showInfo(self):
        print("username:%s department:%s sex:%s"%(self.username,self.depart,self.sex))
class Teacher(SchoolMember):
    def __init__(self,username,depart,sex,title):
        SchoolMember.__init__(self, username, depart, sex)
        self.title = title
    def showInfo(self): #override
        print("teacher's title:%s"%self.title)
        super().showInfo()
class Student(SchoolMember):
    def __init__(self,username,depart,sex,major):
        SchoolMember.__init__(self, username, depart, sex)
        self.major = major
    def showInfo(self):
        print("student's major:%s"%self.major)
        super().showInfo()
student1 = Student("Kevin","College of AI", "male","Blockchain engineering")
student1.showInfo()
teacher1 = Teacher("Wu", "College of AI","male","Dean")
teacher1.showInfo()       

class Employee:
    def __init__(self,name="",birth=0): #先创建父类对象，初始化类的属性
        self.name=name
        self.birth=birth
    def get_salary(self,month):        
        if month == self.birth:
            return 100
        else:
            return 0
class SalariedEmployee(Employee):
    def __init__(self,name,birth,salary):
        Employee.__init__(self, name, birth)
        self.salary = salary
    def get_salary(self,month):
        return self.salary+super().get_salary(month)
class HourlyEmployee(Employee):
    def __init__(self,name,birth,salary,hour):
        Employee.__init__(self, name, birth)
        self.salary = salary
        self.hour = hour
    def get_salary(self,month):
        if self.hour>160:
            return self.salary*160+(self.hour-160)*1.5*self.salary+super().get_salary(month)
        else:
            return self.salary*self.hour+super().get_salary(month)
employee = Employee() #先创建父类对象
employee = SalariedEmployee("Kevin",9, 8000)
print("Kevin's salary:%d"%employee.get_salary(9))
employee = HourlyEmployee("Kelly", 12, 170, 50)
print("Kelly's salary:%d"%employee.get_salary(12))
