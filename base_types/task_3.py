"""
Напишите программу, которая выводит на экран числа от 1 до 100.
При этом вместо чисел, кратных трем, программа должна выводить слово Fizz,
а вместо чисел, кратных пяти — слово Buzz.
Если число кратно пятнадцати, то программа должна выводить слово FizzBuzz
"""

for x in range(1, 101):
    s = '';
    if x % 3 == 0:
        s += 'Fizz'
    if x % 5 == 0:
        s += "Buzz"
    if s == '':
        s = x
    print(s, end=' ')

# for x in range(1, 101):
#     s = '';
#     if x % 3 == 0:
#         s += 'Fizz'
#     if x % 5 == 0:
#         s += "Buzz"
#     if s == '':
#         s = "fizz" * (not (x % 3)) + "buzz" * (not (x % 5))
#     print(str(x) * (not (s)) + s)

# try:
#     s = 100 / 0
# except ZeroDivisionError:
#     print("Нельзя делить на 0")
# else:
#     print(f'Все хорошо')
# finally:
#     print('Программа завершена')