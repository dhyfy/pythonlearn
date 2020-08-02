def fact(n,*b):
    s = 1
    for i in range(1, n + 1):
        s = s * i
    for i in b:
        s=s*i
    return s


print(fact(10,3))
print(fact(10,3,5,8))