#Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

num = int(input("Введите целое число от 0 до 9: "))
# Проверяем что ввели

if num == 0:
    result = 0
elif num > 9:
    result = "Вообще-то просили ввести число до 9"
else:
    num_num = num * 10 + num
    num_num_num = num_num * 10 + num
    result = num + num_num + num_num_num

# Выводим результат
print(result)