import pandas as pd
import numpy as np


#pandas- расширение нампи (структурированные массивы), строки и столбцы индексируются метками, не только 
#числовыми значениями

#Series, DataFrame, Index - основные структуры


data = pd.Series([0.5, 0.75, 0.25, 1.0])
print(data)
print("type data:", type(data), end="\n")

print(data.values)
print(data.index)

print('type values: ', type(data.values))
print('type index: ', type(data.index))

print("data 0: ", data[0])
print("data[1:3]:\n", data[1:3])


data = pd.Series(data= [1,2,3,4], index= ['a', 32, 'c' ,'d'])
print(data)
print(data['a':'d':2])

print(data[32: 'd'])


population_city= {
    'city1' : 1081,
    'city2' : 1082,
    'city3' : 1083,
    'city4' : 1084,
    'city5' : 1085
}
population = pd.Series(population_city)
print(population)
print(population['city2':'city5':2])

#series для создания 
#-списков питона или массивов нампи
#-скалярное значение 
#-словари
print("\n\n\n")
#1привести различные способы создания объектов типа series


#data frame

area_dict = {
    'city1' : 1000,
    'city2' : 1001,
    'city3' : 1002,
    'city4' : 1003,
    'city5' : 1004
}

population = pd.Series(population_city)
area = pd.Series(area_dict)

states = pd.DataFrame({
    'population1' : population,
    'area1' : area
})

print(states)


print("index: \n", states.index)
print("values: \n", states.values)
print("columns: \n", states.columns)

print('area1: ', states['area1'])

#способы создания датафрейм:
# - через объекты Series
# - списки словарей
# - словари объектов сериес
# - двумерный массив нампи
# - структурированный массив нампи

# 2. Привести различные способы создания объектов типа DataFrame


#index - способ организации ссылки на  данные объектов сериес и датафрейм, упорядочен и неизменяем

ind = pd.Index([2,3,5,7,11])
print(ind[1])
print(ind[::2])


#ind[1] = 5 - выведет ошибку, тк ИНДЕКС НЕИЗМЕНЯЕМ

indA = pd.Index([1,2,3,4,5])
indB = pd.Index([2,3,4,5, 6])

print('A: ', indA)
print('B: ', indB)
print(indA.intersection(indB))

#выборка данных из series 
#как словарь

data2 = pd.Series([1,5,3,6,5], index= ['a', 'b', 'c', 'd', 'e'])
print('a' in data2)
print('z' in data2)

print('keys: ', data2.keys())
print(list(data.items()))

data2['a'] = 0.1
data2['x'] = 1000
print(data2)

#то есть сериес - как одномерный массив

data3 = pd.Series([1,2,3,4,5], index=[0.1,2,3,4,5])
print("\n\n")
#print(data2[(data2 >= 3) & (data < 7)])
print(data3.loc[0.1])
print(data3.iloc[3])

print(data3, end="\n\n")

print(data3.T)

#атрибуты-индексаторы
area = {
    'city1' : 9000,
    'city2' : 9001,
    'city3' : 9002,
    'city4' : 9003,
    'city5' : 9004
}
pop = pd.Series({
    'city1' : 1000,
    'city2' : 1001,
    'city3' : 1002,
    'city4' : 1003,
    'city5' : 1004
})

data = pd.DataFrame({'area' : area, 'pop' : pop})
print(data)
print(data.T)

rng = np.random.default_rng()
s = pd.Series(rng.integers(0,10,4))
print('\ns:\n', s)
print(np.exp(s))
print(np.sqrt(s))




pop = pd.Series({
    'city1' : 1001,
    'city2' : 1002,
    'city3' : 1003,
    'city41' : 1004,
    'city51' : 1005
})

area = pd.Series({
    'city1' : 9001,
    'city2' : 9002,
    'city3' : 9003,
    'city42' : 9004,
    'city52' : 9005
})

data = pd.DataFrame({'area' : area, 'pop' : pop})
print('\n',data)


#nan = not a number


# 3. Объедините два объекта Series с неодинаковыми множествами ключей (индексов) так, чтобы вместо NaN было установлено значение 1


dfa = pd.DataFrame(rng.integers(0,10,(2,2)), columns=['a', 'b'])
dfb = pd.DataFrame(rng.integers(0,10,(3,3)), columns=['a', 'b', 'c'])
print(dfa)
print(dfb)

print(dfa*dfb)

rng = np.random.default_rng(1)

A = rng.integers(3,10, (3,3))
print(A)
print(A[0])
print(A-A[0])

df = pd.DataFrame(A, columns=['a', 'b', 'c'])
print(df)
print(df.iloc[0])

# 4. Переписать пример с транслирование для DataFrame так, чтобы вычитание происходило по СТОЛБЦАМ


#NA значения NaN, null


#2 способа хранения отсутствующих значений
#индикаторы Nan, None
vall = np.array([1,2,3])
print(vall.sum())

vall = np.array([1,np.nan, 2,3])
print(vall)
print(vall.sum())
print(np.sum(vall))
print(np.nansum(vall))


x = pd.Series(range(10), dtype = int)
print(x)

x[0]  = None
x[1] = np.nan
print(x)

x1 = pd.Series(['a', 'b', 'c'])
print(x1)
x1[0] = None
x1[1] = np.nan
print(x1)


x2 = pd.Series([1,2,3,np.nan, None, pd.NA])
print(x2)


x3 = pd.Series([1,2,3,np.nan, None, pd.NA], dtype = 'Int64')
print(x3)






# 5. На примере объектов DataFrame продемонстрируйте использование методов ffill() и bfill()

