import matplotlib.pyplot as plt
import numpy as np

#plt.show() запускается 1 раз
#создаются объекта класса figure

x = np.linspace(0, 10, 100)

# fig = plt.figure()
# ax = plt.axes()

#plt.subplot(2,1,1)
#ax.plot(x, np.cos(x), color = 'blue')

#цвет: 
# -'blue'


#plt.subplot(2,1,2)
# ax.plot(x, np.sin(x), color= 'green', linestyle='solid')
# ax.plot(x, np.sin(x-1), color= 'red', linestyle = 'dashed')
# ax.plot(x, np.sin(x-2), color= 'magenta', linestyle='dashdot')
# ax.plot(x, np.sin(x-3), color= 'yellow', linestyle ='dotted')
# ax.plot(x, np.sin(x-4), color='black')
# ax.plot(x, np.sin(x-5), color= 'gray')


# fix, ax = plt.subplots(3)
# ax[0].plot(x, np.sin(x))
# ax[1].plot(x, np.sin(x))
# ax[2].plot(x, np.sin(x))

# ax[1].set_xlim(-2,12)
# ax[1].set_ylim(-1.5,1.5)

# ax[2].set_xlim(12,-2)
# ax[2].set_ylim(1.5,-1.5)

# ax[0].autoscale(tight=False)

x = np.linspace(0, 10, 25)
# plt.plot(x, np.sin(x), '.', color='magenta')
# plt.plot(x, np.sin(x)+1, '>', color='magenta')
# plt.plot(x, np.sin(x)+2, 'x', color='magenta')
# plt.plot(x, np.sin(x)+3, '^', color='magenta')
# plt.plot(x, np.sin(x)+4, '--p', color='magenta')



# _______________________________________________________________________
# x = np.linspace(0, 10, 25)
# plt.plot(x, np.sin(x), '--p', markersize=10, markerfacecolor='white', markeredgecolor='black', color='green')
# #скаттер - для каждой точки можем задать отдбельные характеристики
# rng= np.random.default_rng(0)
# col = rng.random(25)
# sizes = 225*rng.random(25)
# plt.scatter(x, np.cos(x), marker='o', c=col, s=sizes)
# plt.colorbar()
# ________________________________________________________________

# ________________________________________
# x = np.linspace(0,10, 40)
# dy = 0.5
# y = np.sin(x) + dy*np.random.randn(40)
# plt.errorbar(x,y,yerr=dy, fmt='.k')
# plt.fill_between(x,y-dy, y+dy, color='green', alpha =0.2)
# ________________________________________
def f(x,y):
    return np.sin(x)**10+2+np.cos(x+x*2+y**1.6)#*np.sin(x)#+np.sin(y*2)

x = np.linspace(0, 5,50)
y = np.linspace(0, 5,30)
X, Y =np.meshgrid(x,y)

Z = f(X,Y)
c= plt.contourf(X,Y,Z, cmap='plasma')
#plt.clabel(c)
#plt.xlim(0, 10)
#plt.ylim(0, 10)
plt.imshow(Z, extent=[0,5, 0,5], cmap='plasma', interpolation='gaussian')
plt.colorbar()

# plt.fill_between()
plt.show()