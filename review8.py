# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 16:01:25 2024

@author: qing
"""
import csv
'''with open('C:/Users/qing/Desktop/test.txt','r',encoding = "utf-8")as f:
    content = f.read()
    print(content)

with open('C:/Users/qing/Desktop/test.txt','r',encoding = "utf-8")as f:
    content = f.readlines()
    print(content)
    print(content[0])
    for i in content:
        print(i,end='')
print()
with open('C:/Users/qing/Desktop/test.txt','w',encoding = "utf-8")as f:
    str = input("please enter string")
    f.write(str)
'''

with open('C:/Users/qing/Desktop/test.csv','w',newline ='',encoding="utf-8")as f:
    squares = [x**2 for x in range(1,101)]
    write_csv = csv.writer(f)
    for item in squares:
        write_csv.writerow([str(item)])

with open('C:/Users/qing/Desktop/test.csv','w',newline ='',encoding="utf-8")as f:
    writer = csv.writer(f)
    writer.writerows([('color','red'),('size','big'),('male','female')])