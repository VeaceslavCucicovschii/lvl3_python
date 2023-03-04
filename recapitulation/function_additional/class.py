class Container:

    def __init__(self):
        self.is_empty = True
        self.value = None

    def __str__(self):
        if self.is_empty == True:
            return "Container is empty"
        else:
            return f"Container<{self.value}>"

def setContainerValue(container, value):
    container.is_empty = False
    container.value = value
    
def unsetContainerValue(container):
    container.is_empty = True
    container.value = None

container_0 = Container()
setContainerValue(container_0, 10)

print(container_0)
