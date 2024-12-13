# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 18:05:03 2024

@author: qing
"""
import math
#3-1计算圆的周长和半径
'''from math import pi
radius = eval(input("enter circle's radius "))
perimeter = 2*pi*radius
area = pi*(radius**2)
print("%.2f"% perimeter)
print("%.2f"% area)'''

#输出整数较大值
'''a = int(input("please enter a "))
b = int(input("please enter b "))
if a<b:
    temp = 0
    temp = a
    a = b
    b = temp
print("%d "%a)'''

#判断成绩合法与否
'''grade = float(input("please enter your grade "))
if grade>=0 and grade<=100:
    print("legal result: %.1f"% grade)
else:
    print("illegal result")'''

#商品打折
'''total = float(input("please enter your total of bill "))
if (total>1000):
    total*=0.9
elif(total<3000):
    total*=0.8
elif(total<8000):
    total*=0.7
elif(total<10000):
    total*=0.6
else:
    total*=0.5
print("after discount:%.2f"%total)'''

#判断象限
'''x = int(input("key one variable x"))
y = int(input("key one variable y"))
if (x>0):
    if (y>0):
        print("first quadrant")
    else:
        print("fourth quadrant")
else:
    if (y>0):
        print("second quadrant")
    else:
        print("third quadrant")'''

#求100~999的水仙花数
'''for i in range(100,1000,1):
    x = int(i/100)
    y = int(i%100/10)
    z = i%10
    if(i==x**3+y**3+z**3):
        print("%d"%i,end=",")'''

#求0.001m的纸张折叠多少次厚度不低于珠穆朗玛峰(8848m)？
'''thickness =0.001
count = 0
while(thickness<8848):
    thickness*=2
    count+=1
print("require to fold %d times to higher than Mount Qomolangma"%count)

#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("%d * %d = %d"%(j,i,j*i),end="\t")
    print()

row = 1
while(row<=9):
    col = 1
    while(col<=row):
        print("%d * %d = %d"%(col,row,col*row),end="\t")
        col+=1
    row+=1
    print()    
'''

#健康状况检查
'''height = float(input("please enter your height(cm) "))
weight = float(input("please enter your weight(kg) "))
standard = (height-150)*0.6+48
overweight_rate = (weight-standard)/standard
if overweight_rate <0.1:
    print("normal")
elif overweight_rate <0.2:
    print("overweight")
elif overweight_rate <0.3:
    print("mild obesity")
elif overweight_rate <0.5:
    print("moderate overweight")
else:
    print("severe overweight")'''
    
#小白兔吃萝卜
'''carrot = 1
for i in range(9,0,-1):
    carrot = (carrot+1)*2
    print("第%d天的胡萝卜数量:%d"%(i,carrot))'''

'''number = eval(input("key in your number "))
if number>=0:
    print("positive number")
else:
    print("negative number")

sum = 0
for i in range(1,101):
    sum+=i;
print("1~100的和为:%d"%sum)'''

#求最大公约数和最小公倍数

result= 0
for i in range(1,101):
    result=result+1/i;
print("%.10f"% result)

'''a =eval(input("please enter a"))
b =eval(input("please enter b"))
c =eval(input("please enter c"))
C = a+b+c
p = C/2
S = math.sqrt(p*(p-a)*(p-b)*(p-c))
print("perimeter:%.2f area:%.2f"%(C,S))'''

#shopping
shampoo = 15
soap = 2
toothbrush = 5

for i in range(1,7):
    for j in range(1,50):
        for k in range(1,20):
            if i*shampoo+j*soap+k*toothbrush == 100:
                print("shampoo:%d soap:%d toothbrush:%d"%(i,j,k))
            
