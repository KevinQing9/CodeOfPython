# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 18:22:40 2024

@author: qing
"""

'''matrix1 = [[1,2,3],[2,3,4],[3,4,5]]
matrix2 = [[5,6,7],[6,7,8],[7,8,9]]

for i in range(0,len(matrix1)):
    for j in range(0,len(matrix1)):
        sum = matrix1[i][j]+matrix2[i][j]
        print(sum)
        #print(sum,end=',')
'''
    
dict1 = {"1":"Monday","2":"Tuesday","3":"Wednesday",
         "4":"Thursday","5":"Friday","6":"Saturday","7":"Sunday"}
keys = dict1.keys()
values = dict1.values()
items = dict1.items()
for i in keys:
    print(i)
print(keys)
print(values)
print(items)

dict2 ={'小明':'4月1日','小红':'1月2日','老王':'4月1日'}
print("小明的生日：",dict2.get('小明'))
dict2['小明'] = '5月1日'
print("小明的生日：",dict2.get('小明'))
dict2.pop('老王')
dict2['小王'] = '10月1日'
for i in dict2.items():
    print(i)

L = [4,7,16,14,15,16,17,18,19,1]
index=-1
while index<len(L)-1:
    index=index+1
    if L[index]==1:
        continue
    elif L[index]==2:
        print(L[index])
        continue
    i=2
    flag=1
    while(i<L[index]):
        if L[index]%i==0:
            flag=0
            break
        i=i+1
    if flag == 1:
        print(L[index])

dict3={'kelly':['female',22],'kevin':['male',23],
       'takahashi':['female',27],'tanaka':['male',33]}
for i in dict3.keys():
    if dict3[i][0]=='female':
        print(i,dict3[i])

L = [10,9,8,7,6,5,4,3,2,1]
#冒泡排序
for i in range(1,len(L)):
    for j in range(0,len(L)-i):
        if L[j]>L[j+1]:
            temp=L[j]
            L[j]=L[j+1]
            L[j+1]=temp
            
for i in L:
    print(i,end=',')


    

    