# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 22:23:38 2024

@author: qing
"""

def Test1():
    Length = eval(input("please enter length "))
    List1 = []
    for i in range(0,Length):
        List1.append(eval(input("please enter number ")))
    List2=[]
    MaxValue = max(List1)
    List2.append(MaxValue)
    MinValue = min(List1)
    List2.append(MinValue)
    List2.append((Length))
    return tuple(List2)

def Test2(n):
    sum1 = 0
    rev = 1
    for i in range(1,n+1):
        rev = rev*i 
        sum1 = sum1+rev
    return sum1

def Test3(m):
    #先编写3~m+1的行确定规律的代码，再对1,2行的特殊情况进行处理
    arr=[1,1]
    for i in range(1,m+1): #每行
        for j in range(1,m-i+1): #打印空格
            print("",end = " ")
        print("1",end=" ")
        if i==1:
            print()
            continue
        elif i==2:
            print("1")
            continue
        temp = []
        temp.append(1)
        for k in range(0,i-2):
            print("%d"%(arr[k]+arr[k+1]),end=" ")
            temp.append(arr[k]+arr[k+1])
        print("1")
        temp.append(1)
        arr=temp

def Test4(m,*args):    #*args 以元组形式存储多余的数 **kwargs 以字典形式存储多余元素值
    MinNumber = m
    for each in args:
        if each<MinNumber:
            MinNumber = each
    print(MinNumber)

def gcd(a,b):
    two =0
    if a%2==0 and b%2==0:
        a=a/2
        b=b/2
        two =two+1
    while a>b:
        a = a-b
    while a<b:
        b= b-a
    if two!=0:
        return two**2*a
    else:
        return a
        
def lcm(m,n):
    return m*n/gcd(m,n)

def descendent(*args):
    list(args)
    args = sorted(args,key=lambda x:-x)
    return args
        
if __name__ == "__main__":
    '''tuple1 = Test1()
    for j in tuple1:
        print(j)
    print(Test2(eval(input())))'''
    Test3(8)
    Test4(1,4,7,2,3)
    print(lcm(5,15))
    print(descendent(3,4,2,7,8,9))
    
    
    
    
