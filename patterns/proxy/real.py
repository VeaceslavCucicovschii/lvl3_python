from random import randint

class RealData:
    def __init__(self):
        pass

    # IMPORTANT !! real proxy works with 2 classes
    # what is written here is a light version of it:

    def __getattr__(self, name):
        if name == "data":
            self.data = []
            for i in range(10_000_000):
                self.data.append(randint(100, 10_000_000))
            
            return self.data

