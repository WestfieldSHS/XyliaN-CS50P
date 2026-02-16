#promt user for expression
expression = input('Expression: ')
#split expression to 3 parts
x, y, z = expression.split(" ")
#float
x = float(x)
z = float(z)
#calculate the result
if y == '+':
    result = x + z
    print(result)
elif y == '-':
    result = x - z
    print(result)

    

    


