#конспект лекции
import numpy as np
import sys
import array
#типы данных в питоне
x = 1
print(type(x))
print(sys.getsizeof(x))

x = 'hello'
print(type(x))

x = True
print(type(x))

l1 = list([])
print(sys.getsizeof(l1))

l2 = list([1,2,3])
print(sys.getsizeof(l2))

l3 = list([1, 'hello', True])
print(sys.getsizeof(l3))



a1 = array.array('i', [1,2,3])
print(type(a1))
print(sys.getsizeof(a1))


 ## 1. Какие еще существуют коды типов?
 
 
 ## 2. Напишите код, подобный приведенному выше, но с другим типом
 
 
 #___________________________________________________________________________#
 
a = np.array([1,2,3,4,5])
print(type(a), a)

aa = np.array([1,2,3.2, 12.3], dtype = int)
print(type(aa), aa)


arr = np.array([range(i, i+3) for i in [2,4,6]])
print(arr)
 
print(f"type of array: {type(arr)}" )

a5  = np.zeros(10, dtype=int)
print(a5, type(a5))

print(np.ones((2,4), dtype=float))

print((np.full((5,5), 3.1415)))

print(np.arange(0, 20, 3)) #печатает от 0 до 20 с шагом 3
print()

print(np.eye(4))

## 3. Напишите код для создания массива с 5 значениями, располагающимися через равные интервалы в диапазоне от 0 до 1

## 4. Напишите код для создания массива с 5 равномерно распределенными случайными значениями в диапазоне от 0 до 1

## 5. Напишите код для создания массива с 5 нормально распределенными случайными значениями с мат. ожиданием = 0 и дисперсией 1

## 6. Напишите код для создания массива с 5 случайнвми целыми числами в от [0, 10)


###МАССИВЫ

np.random.seed(2)

x1 = np.random.randint(100, size = 5)
x2 = np.random.randint(100, size = (5,2))
x3 = np.random.randint(100, size = (5,2,1))

print(x1, end="\n\n")
print(x2)
#print(x3)

#ndim - число размерностей, размер каждой размерности - shape, общ размер массива size
print(x1.ndim, x1.shape, x1.size)


#доступ к элементам массива

#index

aaa = np.array([1,2,3,4,5,6,6])
print(aaa[0])
print(aaa[-2])
aaa[2] = 244
print(aaa)

#Срез: [начальный элемент:конечный:шаг]

a = np.array([1,2,3,4,5,6])

print(a[0:3:1])
print(a[1:-1])
print(a[1::2])

## 7. Написать код для создания срезов массива 3 на 4
## - первые две строки и три столбца
## - первые три строки и второй столбец
## - все строки и столбцы в обратном порядке
## - второй столбец
## - третья строка

b= a[:3]
print(b)

b[0] = 100
print(a)

## 8. Продемонстрируйте, как сделать срез-копию

print("np arrange: ")
a = np.arange(1, 13)
print(a)
print("\n")

print(a.reshape(2, 6))
print(a.reshape(3, 4))

## 9. Продемонстрируйте использование newaxis для получения вектора-столбца и вектора-строки

x = np.array([1,2,3])
y = np.array([4, 5])
z = np.array([6])

print(np.concatenate([x,y,z]))

'''r1 = np.vstack([x,y])#вертикальное склеивание 
print(r1)
print(np.hstack([r1, r1]))
'''

## 10. Разберитесь, как работает метод dstack

## 11. Разберитесь, как работают методы split, vsplit, hsplit, dsplit

#векторизированная операция - независимо к каждому элементу

x = np.arange(10)
print(x)
print(x*2+1)

#Универсальные функции 

# - -  / // ** %

## 12. Привести пример использования всех универсальных функций, которые я привел

#np.abs  sin/cos/tan, exp, log, sinh, 
x = np.arange(5)
y = np.zeros(10)
print(np.multiply(x, 10,out = y[::2]))

print(y)


x = np.arange(1, 5)
print(x, end = "\n\n")
print(np.add.reduce(x))
print(np.add.accumulate(x))

x = np.arange(1, 10)
print(np.add.outer(x,x))
print(np.multiply.outer(x,x))


