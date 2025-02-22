import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl

# ''''                        как будто сглаживает по х и по у            '''
# fig, ax = plt.subplots(2,3,sharey='row', sharex = 'col') #fig - фигура или холст, ax - график внутри холста
# '''       фигура на 2 строки и 3 столбца, т.е. ax - двумерный массив'''

# for i in range(2):
#     for j in range(3):
#         ax[i,j].text(0.5, 0.5, str((i,j)), fontsize=16,ha='center')
        
        #------------------------------
        
# grid = plt.GridSpec(2,3)
# plt.subplot(grid[0,0])  #создается 4 окошка для графиков и распределяются соотв образом
# plt.subplot(grid[0,1:])
# plt.subplot(grid[1,:2])
# plt.subplot(grid[1,2])

mean = [0,0] #среднее значение для х и у
cov=[[1,1], [1,2]]# Это ковариационная матрица, которая описывает взаимосвязь между двумя переменными:
# Диагональные элементы (1 и 2) — это дисперсии каждой переменной.
# Недиагональные элементы (оба равны 1) — это ковариации, показывающие степень зависимости между x и y

rng = np.random.default_rng(1)
x,y = rng.multivariate_normal(mean,cov, 350).T  
#генерится 350 пар значений (х,у) из многомерного нормального распределения с заданными средними
#и ковариацией. .T транспонирует массив, чтобы получить отдельные массивы x и y.

fig = plt.figure()
grid = plt.GridSpec(4,4,hspace=0.2,wspace =0.2)
'''        создается сетка 4 на 4'''


main_ax = fig.add_subplot(grid[:-1, 1:])

'''                                  |убираются х-овые и у-овые подписи координат'''
y_hist =fig.add_subplot(grid[:-1, 0], xticklabels = [],sharey=main_ax)
x_hist =fig.add_subplot(grid[-1, 1:], yticklabels = [], sharex=main_ax)

y_hist.hist(y, 50, orientation='horizontal', color='red' ,histtype='stepfilled')
x_hist.hist(x, 50, orientation='vertical', histtype='step')


main_ax.plot(x,y,'ok', markersize=3, alpha=0.7)
#plt.plot(x,y)   
plt.show()









