import pandas as pd
import numpy as np

index = [
    ('city1', 2010),
    ('city1', 2020),
    ('city2', 2010),
    ('city2', 2020),
    ('city3', 2010),
    ('city3', 2020)
]

population = [
    101,
    201,
    102,
    202,
    103,
    203,
]

pop = pd.Series(population, index = index)
print(pop)

#хотим написать только 2010ый год
print("2010: \n")

print(pop[[i for i in pop.index if i[1] == 2020]])

#MultiIndex

index=pd.MultiIndex.from_tuples(index)
pop = pop.reindex(index)
print("reindex: \n", pop)

print('\n',pop[:, 2020])
print('\n')
pop_df = pop.unstack()
print(pop_df)

print(pop_df.stack())



index = [
    ('city1', 2010,1),
    ('city1', 2010,2),
    
    ('city1', 2020,1),
    ('city1', 2020,2),
    
    ('city2', 2010,1),
    ('city2', 2010,2),
    
    ('city2', 2020,1),
    ('city2', 2020,2),
    
    ('city3', 2010,1),
    ('city3', 2010,2),

    ('city3', 2020,1),
    ('city3', 2020,2)

]

population = [
    101,
    1010,
    201,
    2010,
    102,
    1020,
    202,
    2020,
    103,
    1030,
    203,
    2030,
]

pop = pd.Series(population, index = index)
print(pop)

index = pd.MultiIndex.from_tuples(index)
pop = pop.reindex(index)
print(pop)
print(pop[:, 2010])
print(pop[:, :, 2])

pop_df = pop.unstack()
print(pop_df)
print(pop_df.stack())
 


index = [
    ('city1', 2010,1),
    ('city1', 2010,2),
    
    ('city1', 2020,1),
    ('city1', 2020,2),
    
    ('city2', 2010,1),
    ('city2', 2010,2),
    
    ('city2', 2020,1),
    ('city2', 2020,2),
    
    ('city3', 2010,1),
    ('city3', 2010,2),

    ('city3', 2020,1),
    ('city3', 2020,2)

]

population = [
    101,
    1010,
    201,
    2010,
    102,
    1020,
    202,
    2020,
    103,
    1030,
    203,
    2030,
]

pop = pd.Series(population, index = index)
print(pop)

index = pd.MultiIndex.from_tuples(index)


pop_df = pd.DataFrame({
    'total': pop,
    'something': [ 
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21
    ]
})


print(pop_df)
print(pop_df['total'])
'''
pop_df_1 = pop_df.loc['city1', 'something']
print(pop_df_1)
'''
#1  Разобраться как использовать мультииндексные ключи в данном примере

#создание мультииндексов:
#1)список массивов
i1 = pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], [1,1,2,2]])
print(i1)


#список коржетей, задающих значение индекса в каждой точке
i2 = pd.MultiIndex.from_tuples([('a', 1),('a', 2), ('b',1), ('b',2)])
print(i2)

#декартово произведение обычных индексов
i3 = pd.MultiIndex.from_product([('a', 'b'), (1,2)])
print(i3)

#описание внутреннего представления: levels, codes
i4 = pd.MultiIndex(
    levels = [ 
              ['a','b'],
              [1,2]
              ],
    codes = [
        [0,0,1,1],
        [0,1,0,1]
    ]
)
print(i4)


#уровням можно задать названия 

data = {
    ('city1', 2010): 100,
    ('city1', 2020): 200,
    ('city2', 2010): 1001,
    ('city2', 2020): 2001,
}

s = pd.Series(data)
print(s)
s.index.names = ['city', 'year']
print(s)

index = pd.MultiIndex.from_product([['city1','city2'], [2010,2020]],names=['city', 'year'])
print(index)

columns = pd.MultiIndex.from_product([['person1','person2', 'person3'], ['job1', 'job2']],names=['worker', 'job'])


rng = np.random.default_rng(1)

data = rng.random((4,6))
print(data)

data_df = pd.DataFrame(data, index = index, columns = columns)
print(data_df)

#2 из получившихся данных выбрать данные по 
# 2020 году для всех столбцов
#job 1для всех строк
# city1, job2




#инлексация и среды по мультиинлексам 
data = {
    ('city1', 2010): 100,
    ('city1', 2020): 200,
    ('city2', 2010): 1001,
    ('city2', 2020): 2001,
    ('city3', 2010): 10001,
    ('city3', 2020): 20001,
}

s = pd.Series(data)
print(s)
s.index.names = ['city', 'year']
print(s['city1', 2010])
print()
print(s['city1'], end='\n\n')

print(s.loc['city1':'city2'])
print(s[:, 2010],end="\n\n")
print(s[s>2000])


# 3. Взять за основу DataFrame со следующей структурой
# index = pd.MultiIndex.from_product(
#     [
#         ['city_1', 'city_2'],
#         [2010, 2020]
#     ],
#     names=['city', 'year']
# )
# columns = pd.MultiIndex.from_product(
#     [
#         ['person_1', 'person_2', 'person_3'],
#         ['job_1', 'job_2']
#     ],
#     names=['worker', 'job']
# )
# 
# Выполнить запрос на получение следующих данных
# - все данные по person_1 и person_3
# - все данные по первому городу и первым двум person-ам (с использование срезов)
#
# Приведите пример (самостоятельно) с использованием pd.IndexSlice

index = pd.MultiIndex.from_product(
    [
    ['a', 'c', 'b'],
    [1,2]
    ]
)


data = pd.Series(rng.random(6),index = index)
data.index.names = ['char', 'int']

print(data)
#print(data['a':'b'])
#ошибка, надо пересортировать.

data = data.sort_index()
print(data)
print(data['a' : 'b'])




index = [
    ('city1', 2010,1),
    ('city1', 2010,2),
    
    ('city1', 2020,1),
    ('city1', 2020,2),
    
    ('city2', 2010,1),
    ('city2', 2010,2),
    
    ('city2', 2020,1),
    ('city2', 2020,2),
    
    ('city3', 2010,1),
    ('city3', 2010,2),

    ('city3', 2020,1),
    ('city3', 2020,2)

]

population = [
    101,
    1010,
    201,
    2010,
    102,
    1020,
    202,
    2020,
    103,
    1030,
    203,
    2030,
]

pop = pd.Series(population, index =index)
print(pop)

i = pd.MultiIndex.from_tuples(index)
pop = pop.reindex(i)
print(pop)

print(pop.unstack())
print(pop.unstack(level = 0))
print(pop.unstack(level = 1))
print(pop.unstack(level = 2))


#Numpy конкатенация

x= [1,2,3]
y= [4,5,6]
z= [7,8,9]

print(np.concatenate([x,y,z]))

x= [[1,2,3]]
y= [[4,5,6]]
z= [[7,8,9]]
print(np.concatenate([x,y,z]))
print(np.concatenate([x,y,z], axis = 1))
print(np.concatenate([x,y,z], axis = 0))

#Pandas - concat

ser1 = pd.Series(['a', 'b', 'c'], index = [1,2,3])
ser2 = pd.Series(['d', 'e', 'f'], index = [4,5,6])

print(pd.concat([ser1, ser2], verify_integrity= False))
print(pd.concat([ser1, ser2], ignore_index= True))
print(pd.concat([ser1, ser2], keys=['iu', '[p]8979']))

print(pd.concat([ser1, ser2], join = 'outer'))
print(pd.concat([ser1, ser2], join = 'inner'))




#4. Привести пример использования inner и outer джойнов для Series (данные примера скорее всего нужно изменить)
# ser1 = pd.Series(['a', 'b', 'c'], index=[1,2,3])
# ser2 = pd.Series(['b', 'c', 'f'], index=[4,5,6])

# print (pd.concat([ser1, ser2], join='outer'))
# print (pd.concat([ser1, ser2], join='inner'))




