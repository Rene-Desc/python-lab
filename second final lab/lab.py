import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.special import legendre

def task_1():
    plt.title("Полиномы Лежандра")
    for i in range(1,8):
        lb = 'n = '+str(i)
        plt.plot(range(i),legendre(i-1),label = lb)

    plt.legend()
    plt.grid()
    plt.show()



def task_2():
    t = np.linspace(1, 3 * np.pi, 999)
    plt.subplot(2,2,1)
    plt.plot(np.sin(2 * t), np.sin(3 * t),)
    plt.subplot(2,2,2)
    plt.plot(np.sin(3 * t), np.sin(4 * t))
    plt.subplot(2,2,3)
    plt.plot(np.sin(5 * t), np.sin(4 * t))
    plt.subplot(2,2,4)
    plt.plot(np.sin(5 * t), np.sin(6 * t))

    plt.show()



def task_3():
    t = np.linspace(0,  4* np.pi, 2000)
    fig,ax = plt.subplots()
    k = np.arange(21, 1,-0.01)


    line, = ax.plot(np.sin(1 * t), np.sin(k * t))


    def update_data(frame, line,t):
        line.set_xdata( np.sin(t) )
        line.set_ydata( np.sin(1/2 * frame*t) )
        return [line]

    animation = FuncAnimation(
                fig = fig,
                func = update_data,
                frames = k,
                fargs = (line,t),
                interval = 21,
                blit = True,
    )

    plt.show()


def mean_squared_error(real, pred): 
   return ((real - pred)**2).mean()

def task_5():
    real = np.linspace(21,221) 
    pred = np.linspace(21,224) 
    mse = mean_squared_error(real, pred)

    figur = plt.figure()
    arg = figur.add_subplot(111, projection='3d')
    arg.plot(real , pred, mse)


    figur = plt.figure()
    arg = figur.add_subplot(111, projection='3d')
    arg.plot(real, pred, mse)
    arg.set_zscale('log')

    plt.show()
