# импортируем модуль стандартной библиотеки json
import json

# открываем файл на чтение
file_object = open("user.txt")

# загружаем JSON документ с помощью функции load
user = json.load(file_object)

file_object.close()
# теперь в переменной user хранится словарь
user

# мы можем работать с этим объектом
user["age"] # 24
user["name"] # "Monty Python"
user["gender"] # "male"

