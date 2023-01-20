# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет


### без Lambda ###

# num1 = int(input('Введите первое число - '))
# num2 = int(input('Введите второе число - '))
# print(f'{num1}, {num2} ->',end = ' ')

# if num1 **2 == num2 or num2**2 == num1:
#     print('да')
# else:
#     print ('нет')


### с Lambda ###
num1 = int(input('Введите первое число - '))
num2 = int(input('Введите второе число - '))

mult = lambda x: x**2

if (mult(num2) == num1) or (mult(num1) == num2): 
    print('Да')
else: print('Нет')