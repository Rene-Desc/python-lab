import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
import numpy as np


fig, (ax1, ax2, ax3) = plt.subplots(3, 1,sharex=True,sharey=True)

ax1.set_xlim(0, 4)
ax1.set_ylim(-4, 4)


line1, = ax1.plot([], [], color='r')
line2, = ax2.plot([], [], color='g')
line3, = ax3.plot([], [], color='b')


def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    return line1, line2, line3

def animate(i):
    global slider1
    global slider2
    global slider3
    global slider4

    omega1 = slider1.val
    frequency1 = slider2.val

    
    omega2 = slider3.val
    frequency2 = slider4.val

    x1 = np.linspace(0, 4, 1000)
    y1 = np.sin(frequency1 * np.pi * (omega1*x1 - 0.06 * i))
    line1.set_data(x1, y1)

    x2 = np.linspace(0, 4, 1000)
    y2 = np.sin(frequency2 * np.pi * (omega2* x2 - 0.04 * i))
    line2.set_data(x2, y2)

    x3 = np.linspace(0, 4, 1000)
    y3 = np.sin(frequency1 * np.pi * (omega1*x3 - 0.06 * i)) + np.sin(frequency2 * np.pi * (omega2 * x3 - 0.04 * i))
    line3.set_data(x3, y3)
    
    return line1, line2, line3

axes_slider1 = plt.axes([0.04, 0.91, 0.86, 0.04])
slider1 = Slider(axes_slider1,
                    label='omega1',
                    valmin=0.1,
                    valmax=1.0,
                    )

axes_slider2 = plt.axes([0.04, 0.96, 0.86, 0.04])
slider2 = Slider(axes_slider2,
                    label='frequency1',
                    valmin=1.0,
                    valmax=2.0,
                    )



axes_slider3 = plt.axes([0.04, 0.01, 0.86, 0.04])
slider3 = Slider(axes_slider3,
                        label='omega2',
                        valmin=0.1,
                        valmax=1.0,
                        )

axes_slider4 = plt.axes([0.04, 0.05, 0.86, 0.04])
slider4 = Slider(axes_slider4,
                        label='frequency2',
                        valmin=1.0,
                        valmax=2.0,
                        )



anim1 = FuncAnimation(fig, animate, init_func=init,
                    frames=211, interval=20, blit=True)
plt.show()
