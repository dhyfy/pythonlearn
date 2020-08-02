# 请在...补充一行或多行代码

def cmul(*p):
    s=1
    for i in p:
        s=s*i
    return s
    ...

print(eval("cmul({})".format(input())))