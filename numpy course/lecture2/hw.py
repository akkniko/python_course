import numpy as np 


a = np.ones((3,2))
b = np.arange(3)
# 2 (3,2) -> (3,2)
# 1 (3, ) -> (1,3) -> (3,3)  
#c = a+b

# 01: что надо изменить в последнем примере чтобы он работал без ошибок
#нужно изменить размер б, тогда получится массив с 3*2

a = np.ones((3,2))
b = np.arange(3).reshape(3,1)
c = a+b
print(c)


## 02: пример для у. вычислять количество элементов по обоим ращмерностям, значения которых больше 3 и меньше 0

y = np.array([[1,2,3], [4,5,6], [7,8,9]])

condition = ((y > 3) & (y < 9))

condition_line = np.sum(condition, axis = 1)
condition_column = np.sum(condition, axis = 0)

print("Кол-во элементов по строкам: ", condition_line, end='\n')
print("Кол-во элементов по столбцам: ", condition_column, end= '\n')



