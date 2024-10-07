number = input("Введите четырёхзначное число: ")

first_digit = int(number[0])
second_digit = int(number[1])
third_digit = int(number[2])
last_digit = int(number[3])

if first_digit + last_digit == second_digit - third_digit:
    result = "yes"
else:
    result = "no"
    
