# Объявляем функцию foo
def foo():  # она не принимает аргументов, поэтому список параметров пуст
    print("Функция foo") # тело функции состоит из одной команды print

# Определим еще функцию bar
def bar(a, b): # она принимает 2 параметра a и b
    print("Функция bar принимает 2 аргумента") # тело функции состоит из одной команды
    print(a)
    print(b)

def tell_even(num):
    if num % 2 == 0:
        print(num, "-- чётно")
    else:
        print(num, "-- нечётно")

def greet(name, gender):
    """Приветствует пользователя по имени в соответствии с полом."""
    if gender == "male":
        print("Hello, Mr ", name)
    elif gender == "female":
        print("Hello, Ms ", name)

def sum_numbers(x, y):
    result = x + y
    return result