# Задание 4:
# Пользователь вводит целое положительное число.'
# Найдите самую большую цифру в числе.'
# Для решения используйте цикл  whilе и арифметические операции')
user_var = int(input('---> введите любое число '))
print('# Вы ввели',user_var )
count = 0
while user_var > count:
      digit = user_var % 10
      if digit > count:
         count = digit
      user_var =  user_var // 10
print('# И самая большая цифра в этом числе', count)