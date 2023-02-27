def increaseInt(n):
    n += 1
    return n


n = 1
n = increaseInt(n)

print(n)

#  n = [new variable] (1)
#  |
#  v
# func(arg)
#  |
#  v
# arg += 1 ~~~> arg = [new variable] (2)