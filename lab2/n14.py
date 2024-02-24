num = -1
nums = 0
total = 0

while num != 0:
    num = int(input("Введите число или 0 для выхода: "))
    if num == 0:
        break
    else:
        nums += 1
        total += num
print(f'Кол-во чисел: {nums}')
print(f'Сумма чисел: {total}')

