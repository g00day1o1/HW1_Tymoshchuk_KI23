import numpy as np

# 1. Створення двовимірного масиву 3x3 з випадкових цілих чисел від 1 до 100
array = np.random.randint(1, 101, size=(3, 3))

# 2. Обчислення суми всіх елементів масиву
sum_elements = np.sum(array)

# 3. Знаходження максимального та мінімального значення в масиві та їх індексів
max_value = np.max(array)
min_value = np.min(array)
max_index = tuple(int(i) for i in np.unravel_index(np.argmax(array), array.shape))  # Перетворення на цілі числа
min_index = tuple(int(i) for i in np.unravel_index(np.argmin(array), array.shape))  # Перетворення на цілі числа

# 4. Сортування масиву по кожному рядку
sorted_array = np.sort(array, axis=1)

# Виведення результатів
print("Масив 3x3:")
print(array)
print("\nСума всіх елементів масиву:", sum_elements)
print(f"Максимальне значення: {max_value}, індекс: {max_index} (i - рядок, j - стовпець)")
print(f"Мінімальне значення: {min_value}, індекс: {min_index} (i - рядок, j - стовпець)")
print("\nМасив, відсортований по кожному рядку:")
print(sorted_array)
