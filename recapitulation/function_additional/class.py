class Container:
    is_empty = True
    value = None

    def setContainerValue(self, value):
        self.value = value
        self.is_empty = False
    
    def unsetContainerValue(self):
        self.value = None
        self.is_empty = True

    def __str__(self):
        if self.is_empty == True:
            return "Container is empty"
        else:
            return f"Container<{self.value}>"

container_0 = Container()
container_0.setContainerValue(10)

print(container_0)