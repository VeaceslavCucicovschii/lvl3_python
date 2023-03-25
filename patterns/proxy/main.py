from real import *

rd = RealData()

localData = [1, 2, 3]

sum = sum(localData)

if input("add the [0] value from the real data ? ") == "y":
    sum += rd.data[0]

print(f"the sum is = {sum}")