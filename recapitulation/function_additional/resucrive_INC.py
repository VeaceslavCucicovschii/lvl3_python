def decreaseInt(n):
    n -= 1
    if n != 0:
        print(n, end=' ')
        return decreaseInt(n)
    else:
        return n
    
n = 8
n = decreaseInt(n)