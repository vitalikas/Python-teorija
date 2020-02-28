# импортируем модуль стандартной библиотеки json
import json

# открываем файл users.txt на чтение
fp = open("users.txt")

# загружаем список пользователей
users = json.load(fp)

# пока мы не начали обработку списка, заводим пустую переменную, в которой будем хранить первого пользователя
first_reg_time = None
last_reg_time = None

# с помощью цикла for итерируемся по всем пользователям
for user in users:
	# если первый пользователь еще не инициализирован или текущий пользователь зарегистрирован раньше, сохраняем текущего пользователя цикла в переменную first_user
	if first_reg_time is None or user["registered"] < first_reg_time["registered"]:
		first_reg_time = user
	if last_reg_time is None or user["registered"] > last_reg_time["registered"]:
		last_reg_time = user

# после завершения цикла, в переменной first_reg_time хранится искомый пользователь
print(first_reg_time)
print(last_reg_time)

# или с while, самый последний

last_reg_time = users[0]["registered"] # у reg_time значение должно быть самое большое
i = 0

while i < len(users):
	if users[i]["registered"] > last_reg_time:
		last_reg_time = users[i]["registered"]
	i = i +1

print(last_reg_time)