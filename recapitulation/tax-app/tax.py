def calculateTax(sum, procent, goal):
    
    """verify if the type of variables was set correctly"""
    
    if type(sum) != float or type(procent) != float or type(goal) != str:
        raise TypeError("incorect type of variable(s)")

    """initializating the declared variable named 'impozit' by calculating the 'procent' amount of money from 'sum'"""
    
    impozit = (procent * sum) / 100

    """constructing the dict structure named 'tax'"""
    
    tax = dict([
        ('sum', sum),
        ('procent', procent),
        ('goal', goal),
        ('impozit', impozit)
    ])

    # dict ! deoarece: 
    # 1. 'dict' proposes a key with which we can separate the scope of each variable
    # 2. We cant construct a 'list' with diferent tipes of variables, for example str and int, while with dict we can

    """return the structure"""
    
    return tax
