# SUBPLOTS/ CONTINUOS FUNCTION

import numpy as np
import matplotlib.pyplot as plt

xstart=0
xstop=2*np.pi
increment=0.1

x=np.arange(xstart,xstop,increment)
y=np.sin(x)
z=np.cos(x)

plt.subplot(211)
plt.plot(x,y,'green')
plt.title('sin')
plt.xlabel('x')
plt.ylabel('sin(X)')
plt.grid()
plt.show()

plt.subplot(212)
plt.plot(x,z,'red')
plt.title('cos')
plt.xlabel('x')
plt.ylabel('cos(Y)')
plt.grid()
plt.show()