class Subscriber:

    def __init__(self, name):
        self.name = name

    def update(self):
        print(f"{self.name} GOT THE NOTIFICATION !")

    def __str__(self):
        return f"COMPANY: {self.name}"

    def __repr__(self):
        return self.__str__()