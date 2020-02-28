# импортируем модуль стандартной библиотеки json
import json

# создаем словарь с данными пользователя
user = {"name": "Monty Python", "gender": "male", "age": 27}

# открываем на запись файл user.txt
file_object = open("user.txt", "w")

# сохраняем словарь user в объект файла file_object
json.dump(user, file_object)

# закрываем объект файла
file_object.close()