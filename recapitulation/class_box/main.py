class Box:

    def __init__(self, *inp):
        if len(inp) == 0:
            self.value = None
        elif len(inp) == 1:
            self.value = inp[0]
        else:
            raise Exception("Sorry, no values more than 1")

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value 

    def __eq__(self, other):
        return self.value == other.value 

    def isEmpty(self):
        if self.value == None:
            return True
        else:
            return False


b1 = Box(100)
b2 = Box(50)

print(b1.value)

if b1 == b2:
    print('b1 = b2')
elif b1 > b2:
    print('b1 > b2')
else:
    print('b1 < b2')