# В переменной хранится имя файла с секретом
FILENAME = 'secret.txt'

# Открываем файл на чтение
secret_file = open(FILENAME)

# Читаем содержимое файла
secret = secret_file.read().strip()

# Приводим полученную строку к типу int
secret = int(secret)

for attempt in range(10, 0, -1):
	# cохраняем в переменную guess ввод пользователя
    guess = input('Угадай загаданное число, у тебя {} попыток. '.format(attempt))
    # функция input вне зависимости от ввода пользователя возвращает строку, поэтому ее нужно привести к типу int
    guess_number = int(guess)
    # если пользователь угадал загаданное число
    if guess_number == secret:
    	# выводим на экран соответствующее сообщение и выходим из цикла
        print('Верно!')
        break
    # если же пользователь ошибся, распечатываем подсказку и продолжаем цикл
    elif guess_number < secret:
        print('Я загадал число больше, попробуй еще раз.')
    else:
        print('Я загадал число меньше, попробуй еще раз.')
