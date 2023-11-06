import numpy as np
import matplotlib.pyplot as plt

xstart=0
xstop=100
radius=7
increment=np.pi*2*radius

x=np.arange(xstart,xstop,increment)
y=np.sin(x)
z=np.cos(x)


plt.subplot(212)
plt.plot(x,y,'g')
plt.title('Sin')
plt.xlabel('X')
plt.ylabel("Sin(x)")
plt.grid()
plt.legend()
plt.show()

plt.subplot(212)
plt.plot(x,z,'red')
plt.title('Cos')
plt.xlabel('X')
plt.ylabel("Cos(x)")
plt.grid()
plt.legend()
plt.show()
