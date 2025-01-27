# 1. Привести различные способы создания объектов типа Series
# Для создания Series можно использовать
# - списки Python или массивы NumPy
# - скалярные значение
# - словари

import pandas as pd
import numpy as np

series_from_list = pd.Series([1, 2, 3, 4])
series_from_array = pd.Series(np.array([5, 6, 7, 8]))
series_from_scalar = pd.Series(10, index=[0, 1, 2, 3])
series_from_dict = pd.Series({'a': 1, 'b': 2, 'c': 3})



# 2. Привести различные способы создания объектов типа DataFrame
# DataFrame. Способы создания
# - через объекты Series
# - списки словарей
# - словари объектов Series
# - двумерный массив NumPy
# - структурированный массив Numpy

df_from_series = pd.DataFrame({'col1': pd.Series([1, 2, 3]), 'col2': pd.Series([4, 5, 6])})
df_from_list_of_dicts = pd.DataFrame([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}])
df_from_dict_of_series = pd.DataFrame({'col1': pd.Series([1, 2, 3]), 'col2': pd.Series([4, 5, 6])})
df_from_np_array = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]), columns=['a', 'b', 'c'])
structured_array = np.array([(1, 'Alice'), (2, 'Bob')], dtype=[('id', 'int32'), ('name', 'U10')])
df_from_structured_array = pd.DataFrame(structured_array)

# 3. Объедините два объекта Series с неодинаковыми множествами ключей (индексов) так, чтобы вместо NaN было установлено значение 1
df1 = pd.Series({
    'city1' : 1,
    'city2' : 2,
    'city3' : 3
})
df2 = pd.Series({
    'city11' : 1,
    'city22' : 2,
    'city33' : 3,
    'city44' : 4
})
dff = pd.concat([df1, df2]).fillna(1)
print(dff)

# 4. Переписать пример с транслирование для DataFrame так, чтобы вычитание происходило по СТОЛБЦАМ

rng = np.random.default_rng(1)
A = rng.integers(3, 10, (3, 3))
df = pd.DataFrame(A, columns=['a', 'b', 'c'])
print("\nDF:")
print(df)

res = df - df.iloc[:, 0] 
print(res.fillna(1))

# 5. На примере объектов DataFrame продемонстрируйте использование методов ffill() и bfill()

data = {
    'a': [1, 2, 3, np.nan],
    'b': [np.nan, 2, np.nan, 4],
    'c': [1, 2, np.nan, np.nan]
}
df = pd.DataFrame(data)
print("исходный DF: ")
print(df)
ffilled_df = df.ffill()

print("\nПосле ffill:")
print(ffilled_df)

bfilled_df = df.bfill()
print("\nПосле bfill:")
print(bfilled_df)

