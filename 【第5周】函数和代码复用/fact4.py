def fact(n,m=1):
    s = 1
    for i in range(1, n + 1):
        s = s * i
    return s//m,m,n


print(fact(10))
print(fact(10,2))