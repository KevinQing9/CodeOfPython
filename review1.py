# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 17:52:40 2024

@author: qing
"""

'''name = input("please enter name ");
height = eval(input("please enter height(m) "))
weight = eval(input("please enter weight(kg) "))
BMI = weight/(height*height);
print("name%s:"%name)
print("height(m):%.2f weight(kg):%.2f BMI:%.2f"%(height,weight,BMI))'''

'''dollar = eval(input("please enter US dollar amount$: "))
ExchangeRate = 6.70
RMB = ExchangeRate*dollar
print("before exchanging:{0} 1dollar; after exchanging:{1:.2f}".format(dollar, RMB))
print(f"before exchanging:{dollar} 1dollar; after exchanging:{RMB:.2f}")
str1 = "1234"
result = input("please enter string ")
#str1[0] = 3
print("third place:",result[2])
print("odd string:",result[0::2])
print("from third place to end:",result[3:-1:])
print("{}".format(str1))
print(r"C:/desktop/admin")'''

'''import math
a = eval(input("请输入一个直角边"))
b = eval(input("请输入另一个直角边"))
c = math.sqrt(a**2 + b**2)
print("斜边为:{0:.2f}".format(c))'''

'''a = eval(input("please enter one number a: "))
b = eval(input("please enter another number b: "))
print(f"before swaping a={a} b={b}")
m = a
a = b
b = m
print(f"after swaping a={a} b={b}")'''

print("hello,this is good habit \\n")

string =input()
string = string[::-1]
print(string)

string = input()
print("0出现次数%d 出现频率%.2f"%(string.count("0"),string.count("0")/len(string)))

string = input()
print(f"替换前{string}")
#string.replace("a", "A") ***原地替换
string = string.replace("a", "A")
print(f"替换后{string}")

second = 145894
d = second//(24*3600)
h = second%(24*3600)//3600
m = second%(24*3600)%3600//60
s = second%(24*3600)%3600%60
print("%d天 %d时 %d分钟 %d秒"%(d,h,m,s))





