# Задание 3: '
# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.
user_digit = int(input('---> Выбирите цифру от 0 до 9'))
digits_var = ((100 * user_digit) + (10 * user_digit) + user_digit) + ((10 * user_digit) + user_digit) + user_digit
print ('Результат для цифры',user_digit,'будет равен',digits_var)
