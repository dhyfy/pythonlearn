s=0
for i in range(2,101):
    f=1
    if i==2:
        f=1
    else:
        for j in range(2,i):
            if i%j==0:
                f=0
                break;
    if f==1:
        s=s+i
print(s)