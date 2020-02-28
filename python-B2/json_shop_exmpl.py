# импортируем модуль стандартной библиотеки json
import json

# открываем файл customers.txt на чтение
file_object = open("customers.txt")

# загружаем JSON документ с помощью функции load
customers = json.load(file_object)
file_object.close()

# в переменной customers теперь хранится список
customers
# [{"name": "Alice", "gender": "female", "email": "alice@example.com"}, {"name": "Bob", "gender": "male", "email": "bob24@exa.net"}, {"name": "John", "gender": "female", "email": "john@johnjefferson.org"}]

# выведем на экран первый элемент этого списка
customers[0]
# {"name": "Alice", "gender": "female", "email": "alice@example.com"}

# С помощью цикла for итерируемся по списку customers
for customer in customers:
	# проверяем значение поля gender на равенство строке female
	if customer['gender'] == "female":
		# распечатываем на экран
		print(customer)