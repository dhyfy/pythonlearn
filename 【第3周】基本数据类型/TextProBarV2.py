import time
scale = 100
print('执行开始......')
for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i / scale) * 100
    print('\r{:^3.0f}%[{}->{}]'.format(c, a, b),end="")
    time.sleep(0.1)
print('执行结束......')