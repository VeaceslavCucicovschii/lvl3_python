class Container:
    is_empty = True
    value = None

    def __str__():
        if Container.is_empty == True:
            return "Container is empty"
        else:
            return f"Container<{Container.value}>"

def setContainerValue(value):
    Container.is_empty = False
    Container.value = value
    
def unsetContainerValue():
    Container.is_empty = True
    Container.value = None

setContainerValue(10)

print(container_0)
