# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.


### без filter ###

# user_number = int(input('Enter your number: '))
# if (user_number % 5 == 0 and user_number % 10 == 0 or user_number % 15 == 0) and user_number != 30:
#     print('Your number is nice! :)')
# else:
#     print('Try again.')


### с filter ###
user_number = int(input('Enter your number: '))
user_number_list = []
user_number_list.append(user_number)

def kratnost(x):
    if (x % 5 == 0 and x % 10 == 0 or x % 15 == 0) and x != 30:
        return True
    else:
        return False
result = filter (kratnost,user_number_list) 
# print(list(result))
if  len(list(result))>0:
    print('Your number is nice! :)')
else:
    print('Try again.')
