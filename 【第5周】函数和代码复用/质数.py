# 请在...补充一行或多行代码

def prime(m):
    f=1
    if m<=1:
        f=0
    elif m==2:
        f=1
    else:
        for i  in range(2,m):
            if m%i==0:
                f=0
                break
    
    return f



n = eval(input())
m=int(n)
if n>m:
    n=m+1
num=0
while num<5:
    if prime(n)==1:
        num+=1
        if num!=5:
            print(n,end=",") 
        else:
            print(n)
    n+=1
