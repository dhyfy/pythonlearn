count = 0


def hanoi(n, src, dst, mid):
    global count
    if n == 1:
        count += 1
        print('step {}:plate {} from {} to {}'.format(count, n, src, dst))
    else:
        hanoi(n - 1, src, mid, dst)
        count += 1
        print('step {}:plate {} from {} to {}'.format(count, n, src, dst))
        hanoi(n - 1, mid, dst, src)


hanoi(3, 'A', 'B', 'C')
