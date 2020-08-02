n=1000
while n<10000:
    qian=n//1000
    bai=n//100%10
    shi=n//10%10
    ge=n%10
    if pow(qian,4)+pow(bai,4)+pow(shi,4)+pow(ge,4)==n:
        print(n)
    n=n+1