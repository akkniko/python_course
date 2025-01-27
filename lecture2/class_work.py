import numpy as np
#Суммирование  значений и другие функции

rng = np.random.default_rng(1)
s = rng.random(50)
print(s)
print(sum(s))
print(np.sum(s))

a = np.array([[1,2,3,4,5], 
            [6,7,8,9,10]])
print('sum a = ', np.sum(a), end = " \n")
print('sum a0 = ', np.sum(a, axis = 0), end = " \n")#сумма по столбцам
print('sum a1 = ', np.sum(a, axis = 1), end = " \n")#сумма по строкам

print("\n")

print('min a = ', a.min(), end = " \n")
print('min a0 = ', a.min(0), end = " \n")#min по столбцам
print('min a1 = ', a.min(1), end = " \n")#min по строкам

print("\n")

#nan- not a number
print('sum a = ', np.nanmin(a), end = " \n")
print('sum a0 = ', np.nanmin(a, axis = 0), end = " \n")#сумма по столбцам
print('sum a1 = ', np.nanmin(a, axis = 1), end = " \n")#сумма по строкам




#Транслирование - broadcasting
#набор правил, которые позводяют осуществлять бинарные операции с массивами разных форм и размеров

a1 = np.array([0,1,2])
b1 = np.array([5,5,5])

print(a1+b1)
print(a1 + 5)


a = np.array([0, 1,2])
b = np.array([[0], [1], [2]])
c = a+b #т.е. будет размерность 3 на 3
print(c)
#Правила
#1 если размерности массивов отличаются, то форма массива меньше размерности дополняется 1 с левой стороны
#2 если формы массивов не совпадают в каком то измерении, то если у массива форма  = 1,
# то он растягивается до формы 2го
#3 если в каком либо измерении  размеры отличаются и ни один ищ них не 1, то генерируется ошибка    

a = np.array(([1,2,3], [3,4,5]))
b = np.array([5])
print(a.ndim, a.shape)
print(b.ndim, b.shape)

#a         (2,3)
#b (1,) -> (1.1) -> (2,3)

a2 = np.ones((2,3))
b = np.arange(5)


print(a2)
print(b)

print(a2.ndim, a2.shape)
print(b.ndim, b.shape)

 
a3 = np.arange(3).reshape(3,1) #столбец 3 на 1
b = np.arange(3)

print(a3)
print(b)
c = a3+b
print(c) #т.е. с растянулся до размера 3 на 3
print(c.shape)

#__________________________

a = np.ones((3,2))
b = np.arange(3)
# 2 (3,2) -> (3,2)
# 1 (3, ) -> (1,3) -> (3,3)  
#c = a+b

# 01: что надо изменить в последнем примере чтобы он работал без ошибок


x = np.array([
    [1,2,3,4,5,6,7,8,9],
    [9,8,7,6,5,4,3,2,1]
])

xmean0 = x.mean(0)#получили среднее значение по нулевому элементу
print(x)
xcenter0 = x - xmean0 #центрирование массивов 
print(xcenter0)

xmean1 = x.mean(1)#получили среднее значение по нулевому элементу
print(x)
xmean1 = xmean1[:, np.newaxis]
xcenter1 = x - xmean1 #центрирование массивов 
print(xcenter1)

x = np.linspace(0, 7, 100)
y = np.linspace(0, 7, 100)[:, np.newaxis]

z = np.cos(x)** 2 + np.sin(30+x*y)*np.sin(y)
print(z.shape)

import matplotlib.pyplot as plt

#plt.imshow(z)
#plt.colorbar()
#plt.show()



x = np.array([1,2,3,4,5])
x = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print(x<3)
print(np.less(x,3))

print(np.sum(y<4, axis = 0))
print(np.sum(y<4, axis = 1))
print(np.sum(y<4))


## 02: пример для у. вычислять количество элементов по обоим ращмерностям, значения которых больше 3 и меньше 9

#маски - булевы массивы  
x = np.array([1,2,3,4,5])
y = print(x<3)

print(x[x<3])

print(bin(42))
print(bin(59))

print(bin(42 & 59))

#векторизация индекса

x = np.arange(10)
i = np.array([2,4,7])

print(x)
x[i] = 100

print(x)


##сортировка массивов

x = [3,2,3,5,2,5,6,7,8]
print(sorted(x))
print(np.sort(x))

#структурированные массивы
data = np.zeros(4, dtype = {'names':('name', 'age'), 'formats':('U10', 'i4')})
name = ['name1', 'name2', 'name3', 'name4']
age = [10, 20, 30, 40]
data['name'] = name
data['age'] = age
print(data)

print(data.dtype)


print(data['age'] > 20)
print(data[data['age'] > 20] ['name'])

#массивы записей
data_rec = data.view(np.recarray)
print(data_rec)
print(data_rec[0])
print(data_rec[-1].name)









