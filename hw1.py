## 1. Какие еще существуют коды типов?

import array
import numpy as np
import random

#целые числа
a1 = array.array('i', [1, 2, 3])
print(a1)

# Массив чисел с плавающей точкой (float)
a2 = array.array('f', [1.0, 2.0, 3.0])
print(a2)

# Массив символов (char)
a3 = array.array('b', [65, 66, 67]) 
print(a3)

a4 = array.array('L', [65, 66, 67]) 
print(a4)

## 2. Напишите код, подобный приведенному выше, но с другим типом
import sys
import array

a2 = array.array('f', [1.5, 2.5, 3.5])
print("Тип массива a2:", type(a2))
print("Размер массива a2 в байтах:", sys.getsizeof(a2))

a3 = array.array('d', [1.5, 2.5, 3.5])
print("Тип массива a3:", type(a3))
print("Размер массива a3 в байтах:", sys.getsizeof(a3))

a4 = array.array('b', [1, 2, 3])
print("Тип массива a4:", type(a4))
print("Размер массива a4 в байтах:", sys.getsizeof(a4))

## 3. Напишите код для создания массива с 5 значениями, располагающимися через равные интервалы в диапазоне от 0 до 1
arr = np.linspace(0, 0.9, 5)
print(arr)

## 4. Напишите код для создания массива с 5 равномерно распределенными случайными значениями в диапазоне от 0 до 1
arr2 = np.random.uniform(0, 0.9, 5)
print(arr2)

## 5. Напишите код для создания массива с 5 нормально распределенными случайными значениями с мат. ожиданием = 0 и дисперсией 1

arr3 = np.random.normal(0, 1, 5)
print(arr3)

## 6. Напишите код для создания массива с 5 случайнвми целыми числами в от [0, 10)
arr4 = np.random.randint(0, 10, 5)
print(arr4)

## 7. Написать код для создания срезов массива 3 на 4
## - первые две строки и три столбца
## - первые три строки и второй столбец
## - все строки и столбцы в обратном порядке
## - второй столбец
## - третья строка

# Создаём массив 3x4
array = np.arange(12).reshape(3, 4)
print("Исходный массив:\n", array)

# Первые две строки и три столбца
slice1 = array[:2, :3]
print("\nПервые две строки и три столбца:\n", slice1)

# Первые три строки и второй столбец
slice2 = array[:3, 1]
print("\nПервые три строки и второй столбец:\n", slice2)

# Все строки и столбцы в обратном порядке
slice3 = array[::-1, ::-1]
print("\nВсе строки и столбцы в обратном порядке:\n", slice3)

# Второй столбец
slice4 = array[:, 1]
print("\nВторой столбец:\n", slice4)

# Третья строка
slice5 = array[2, :]
print("\nТретья строка:\n", slice5)


## 8. Продемонстрируйте, как сделать срез-копию

# Создаём массив
original_array = np.array([1, 2, 3, 4, 5])

# Создаём срез-копию
slice_copy = original_array[:]

# Изменяем копию
slice_copy[0] = 99

print("Оригинальный массив:", original_array)
print("Срез-копия:", slice_copy)


## 9. Продемонстрируйте использование newaxis для получения вектора-столбца и вектора-строки

# Создаём одномерный массив
vector = np.array([1, 2, 3])

# Вектор-строка
vector_row = vector[np.newaxis, :]
print("\nВектор-строка:\n", vector_row)

# Вектор-столбец
vector_column = vector[:, np.newaxis]
print("\nВектор-столбец:\n", vector_column)


## 10. Разберитесь, как работает метод dstack

# Два массива одинаковой формы
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

# Используем dstack
stacked = np.dstack((array1, array2))
print("\nРезультат dstack:\n", stacked)

## 11. Разберитесь, как работают методы split, vsplit, hsplit, dsplit

# Создаём массив 4x4
array = np.arange(16).reshape(4, 4)

# split — делим вдоль одной оси
split_arrays = np.split(array, 2, axis=0)
print("\nРезультат split по оси 0:\n", split_arrays)

# vsplit — делим по вертикали
vsplit_arrays = np.vsplit(array, 2)
print("\nРезультат vsplit:\n", vsplit_arrays)

# hsplit — делим по горизонтали
hsplit_arrays = np.hsplit(array, 2)
print("\nРезультат hsplit:\n", hsplit_arrays)

# dsplit — делим по глубине (для 3D массива)
array3d = np.arange(24).reshape(2, 3, 4)
dsplit_arrays = np.dsplit(array3d, 2)
print("\nРезультат dsplit:\n", dsplit_arrays)


## 12. Привести пример использования всех универсальных функций, которые я привел

