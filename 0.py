num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
operation = input("Выберите операцию (+, -, *, /): ")
result = 0
if operation == "+":    result = num1 + num2
elif operation == "-":    result = num1 - num2
elif operation == "*":    result = num1 * num2
elif operation == "/":    result = num1 / num2
print (num1,num2,operation,"=",result)

