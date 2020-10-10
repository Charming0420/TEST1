cus = int(input())
find = 1000-cus
x = 0
a1 = find//500
a2 = (find - 500*a1)//100
a3 = (find - 500*a1 - 100*a2)//50
a4 = (find - 500*a1 - 100*a2 - 50*a3)//10
a5 = (find - 500*a1 - 100*a2 - 50*a3 - 10*a4)//5
a6 = (find - 500*a1 - 100*a2 - 50*a3 - 10*a4 - 5*a5)//1
if a1>0:
    print("500, ",a1,end='')
    x = 1
if a2>0:
    if x==1:
        print("; ",end='')
    print("100, ",a2,end='')
    x = 1
if a3>0:
    if x==1:
        print("; ",end='')
    print("50, ",a3,end='')
    x = 1

if a4>0:
    if x==1:
        print("; ",end='')
    print("10, ",a4,end='')
    x = 1

if a5>0:
    if x==1:
        print("; ",end='')
    print("5, ",a5,end='')
    x = 1
    
if a6>0:
    if x==1:
        print("; ",end='')
    print("1, ",a6,end='')
    x = 1    
