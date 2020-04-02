# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:21:16 2020

@author: adiallo
"""
# Thierno Aziz Diallo
'''
Write a program that displays a plot of the functions 
f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
'''
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(1.0 ,4.0, 100) #defines values that will be used for X axis
#x = np.arange (1.0 ,4.0, 100)
y1 = x #Axis values f(x)=x
y2 = x ** 2 #Axis values to power 2, g(x)=x2
y3 = x ** 3 #Axis values to power 3, h(x)=x3

plt.title ("Functions", fontsize = '20') # shows the title for the plot
plt.xlabel ("X", fontsize = 20) #shows the name for x axis
plt.ylabel ("Y", fontsize =20) #shows the name for y axis

plt.plot (x,y1, 'g.', label = "f(x) = x") #Ploting f(x)=x
plt.plot (x,y2, 'y.', label = "g(x) = x**2") #Ploting g(x)=x2
plt.plot (x,y3, 'b.', label = "h(x) = x**3") #Ploting h(x)=x3
plt.legend(loc = 'upper left' , fontsize = '14')
plt.grid(True) # drawving a grid on the plot 

# plt.plot([1, 2, 3, 4])
#plt.ylabel('some numbers')
plt.show() # Display the plot on the screen

'''
Requirements:
To fully run this program, we will need to install numpy and matplolib.
If numpy and matplotlib are not imported will get :
    ModuleNotFoundError: No module name 'numpy'
    ModuleNotFoundError: No module name 'matplotlib'
    
'''
"""
References:
https://www.mathworks.com/help/matlab/ref/fplot.html
https://matplotlib.org/tutorials/introductory/pyplot.html
https://matplotlib.org/api/pyplot_api.html
https://stackoverflow.com/questions/38666527/what-is-the-necessity-of-plt-figure-in-matplotlib
https://scipy-lectures.org/intro/matplotlib/index.html
'''

"""