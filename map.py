# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

### Без Map ###

# num = int(input("Ведите число: "))

# dvoichnoe = "{0:b}".format(num)
# dvoichnoe = bin(num)
# print (dvoichnoe)

### C Map ###


num = int(input("Ведите число: "))
def dvoichnoe(x):
    res = "{0:b}".format(x)
    res = bin(x)
    return res
NewList = [num]
result = map(dvoichnoe, NewList)
print(list(result))