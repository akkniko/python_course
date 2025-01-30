import numpy as np
import pandas as pd

# # 1. Разобраться как использовать мультииндексные ключи в данном примере
# index = [
#     ('city_1', 2010),
#     ('city_1', 2020),
#     ('city_2', 2010),
#     ('city_2', 2020),
#     ('city_3', 2010),
#     ('city_3', 2020),
# ]

# population = [
#     101,
#     201,
#     102,
#     202,
#     103,
#     203,
# ]
# pop = pd.Series(population, index = index)
# pop_df = pd.DataFrame(
#     {
#         'total': pop,
#         'something': [
#             10,
#             11,
#             12,
#             13,
#             14,
#             15,
#         ]
#     }
# )

# ???? ## pop_df_1 = pop_df.loc???['city_1', 'something']
# ???? ## pop_df_1 = pop_df.loc???[['city_1', 'city_3'], ['total', 'something']]
# ???? ## pop_df_1 = pop_df.loc???[['city_1', 'city_3'], 'something']

import pandas as pd

index = [
    ('city_1', 2010),
    ('city_1', 2020),
    ('city_2', 2010),
    ('city_2', 2020),
    ('city_3', 2010),
    ('city_3', 2020),
]

population = [101, 201, 102, 202, 103, 203]

pop = pd.Series(population, index=pd.MultiIndex.from_tuples(index, names=['city', 'year']))

pop_df = pd.DataFrame(
    {
        'total': pop,
        'something': [10, 11, 12, 13, 14, 15]
    }
)

print(pop_df)

pop_df_1 = pop_df.loc['city_1', 'something']
print(pop_df_1)

pop_df_1 = pop_df.loc[['city_1', 'city_3'], ['total', 'something']]
print(pop_df_1)

pop_df_1 = pop_df.loc[['city_1', 'city_3'], 'something']
print(pop_df_1)




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

df_2020 = data_df.loc[(slice(None), 2020), :]
print(df_2020)

data_job = data_df.loc[:, (slice(None),'job1')]
print(data_job)

df_city1_job2 = data_df.loc[('city1', slice(None)), (slice(None), 'job2')]
print(df_city1_job2)


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
    [['city_1', 'city_2'], [2010, 2020]],
    names=['city', 'year']
)

columns = pd.MultiIndex.from_product(
    [['person_1', 'person_2', 'person_3'], ['job_1', 'job_2']],
    names=['worker', 'job']
)

rng = np.random.default_rng(42)
data = rng.random((4, 6))

df = pd.DataFrame(data, index=index, columns=columns)
idx = pd.IndexSlice

result_1 = df.loc[:, idx[['person_1', 'person_3'], :]]

#срезы
result_2 = df.loc[
    idx['city_1', :],         
    idx['person_1':'person_2', :]  
]

#4. Привести пример использования inner и outer джойнов для Series (данные примера скорее всего нужно изменить)
# ser1 = pd.Series(['a', 'b', 'c'], index=[1,2,3])
# ser2 = pd.Series(['b', 'c', 'f'], index=[4,5,6])

# print (pd.concat([ser1, ser2], join='outer'))
# print (pd.concat([ser1, ser2], join='inner'))

ser1 = pd.Series(['a', 'b', 'c'], index=[1, 2, 3])
ser2 = pd.Series(['x', 'y', 'z'], index=[3, 4, 5])

print("ser1:")
print(ser1)
print("\nser2:")
print(ser2)

outer_join = pd.concat([ser1, ser2], join='outer', axis=1)
print(outer_join)

inner_join = pd.concat([ser1, ser2], join='inner', axis=1)
print(inner_join)
