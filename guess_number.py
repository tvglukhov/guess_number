from random import randint

number = randint(1,100)
print('Угадайте число от 1 до 100')

while True:
    guess = int(input('Ваше число: '))
    if guess > number:
        print('Ваше число больше того, что загадано')
    elif guess < number:
        print('Ваше число меньше того, что загадано')
    else:
        print('Отличная интуиция! Вы угадали число :)')
        break