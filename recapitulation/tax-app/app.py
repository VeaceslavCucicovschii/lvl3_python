from tax import calculateTax

salary = float(input("salary = "))

tax = calculateTax(salary, 15.0, 'salary')

print(tax)