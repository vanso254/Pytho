# Simple Hellow world program
# print("Hellow World")

# declaring a variables
# x=3
# y=3*x
# print(y)


# Types in python
# a=1
# b=2.8
# c=1+2j

# print(type(a))
# print(type(b))
# print(type(c))


#STRING METHODS
# a="Hello World"
# print(a)
# print(a[0])
# print(a[2:5])
# print(len(a))
# print(a.lower())
# print(a.capitalize())
# print(a.upper())
# print(a.replace("H","J"))
# print(a.split(" "))

# from math import sin,cos
# x=3.14
# y=sin(x)
# print(y)
# t=cos(x)
# print(t)

# WE CAN CAN ALSO DO IT AS
# import math as mt

# x=3.14
# print(mt.cos(x))

# import numpy as np
# x=3.142
# print(np.sin(x))    

#USING MATPLOTLIB TO DRAW A GRAPH  

# import matplotlib.pyplot as plt

# x = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
# y = [ 5 , 2 ,4 , 4 , 8 , 7 , 4 , 8 , 10 , 9 ] 

# plt.plot(x,y) 

# plt.xlabel('Time(s)')
# plt.ylabel('Temperatue(degC)')
# plt.show()
  
  #A SIN CURVE
# import matplotlib.pyplot as plt
# import numpy as np 

# x = [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7]
# y=np.sin(x)

# plt.plot(x,y)
# plt.xlabel('x')
# plt.ylabel('y')

# plt.show()


# SUBPLOTS

import numpy as np
import matplotlib.pyplot as plt

xstart=0
xstop=2*np.pi