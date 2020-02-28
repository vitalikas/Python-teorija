flowers = {
    "iris_setosa": {
        "sepal_length": [3.6, 4.9, 4.8, 4.7],
        "sepal_width": [2.9, 3.3, 3.2, 3.1],
        "petal_length": [1.3, 1.2, 1.5, 1.4],
    },
    "iris_virginica": {
        "sepal_length": [7.2, 7.0, 7.9],
         "sepal_width": [3.1, 2.7, 2.8],
        "petal_length": [5.5, 5.5, 6.5],
    },
    "iris_versicolor": {
        "sepal_length": [6.5, 6.0, 6.1, 6.2, 6.3],
         "sepal_width": [2.8, 2.9, 2.4, 2.7, 2.7],
        "petal_length": [4.8, 4.7, 5.0, 4.9, 4.8],
    },
}

sum_sepal_length = 0
sum_sepal_width = 0
sum_petal_length = 0

count_values_sepal_length = 0
count_values_sepal_width = 0
count_values_petal_length = 0

for param in flowers.values(): 
    for value in param['sepal_length']:
        sum_sepal_length = sum_sepal_length + value
        count_values_sepal_length = count_values_sepal_length + 1
    for value in param['sepal_width']:
        sum_sepal_width = sum_sepal_width + value
        count_values_sepal_width = count_values_sepal_width + 1
    for value in param['petal_length']:
        sum_petal_length = sum_petal_length + value
        count_values_petal_length = count_values_petal_length + 1

print(sum_sepal_length)
print(count_values_sepal_length)
print(sum_sepal_width)
print(count_values_sepal_width)
print(sum_petal_length)
print(count_values_petal_length)

mean_sepal_length = sum_sepal_length / count_values_sepal_length
print(mean_sepal_length)
mean_sepal_width = sum_sepal_width / count_values_sepal_width
print(mean_sepal_width)
mean_petal_length = sum_petal_length / count_values_petal_length
print(mean_petal_length)