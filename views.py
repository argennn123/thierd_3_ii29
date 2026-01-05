import random

num1 = int(input('Томонку диапазон: '))
num2 = int(input('Жогорку диапазон: '))
num = random.randint(num1, num2)
total = 0
while True:
    found_num = int(input(f'{num1} жана {num2} ортосундагы санды табыныз: '))
    total += 1
    if found_num > num:
        print('Сиз жазган сан чон')
    elif found_num < num:
        print('Сиз жазган сан кичине')

    elif found_num == num:
        print(f'Куттуктайбыз сиз {num} санын {total} иретте таптыныз')
        break