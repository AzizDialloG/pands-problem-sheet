#Thierno Aziz Diallo

#Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
#You should create a function called sqrt that does this.
"""
$ python squareroot.py
Please enter a positive number: 14.5
The square root of 14.5 is approx. 3.8
"""
#Newton Methode.
"""
new_abs= abs- ((abs ** 2 -x)/ (2 * abs))
tolerance= new_abs - abs
"""
import math
def square_num(number):
    result= math.sqrt(number)
    return result
def square_root(x,y,tolerance = 66666): #define functions
    abs = x
    #tolerance = 100
    new_abs=0.001
    count= 0
    
    while tolerance > y:
        new_abs= abs- ((abs ** 2 -x)/ (2 * abs)) #Newton Method
        tolerance= new_abs - abs
        if tolerance < 0:
            tolerance *= -1
            abs = new_abs
            count = count + 1
    print('Square root calculated in', count,"abs")
    return abs

rootsquare = float (input("Please enter a positive number:"))
approx = float (input("Please enter an approximation value (like 0.001 as example:")) #newton formula by calculing square root (approx)
print('The Square root of',rootsquare, 'is approximately %1.f'% round((square_root(rootsquare,approx)),1))#around the decimal places to 1
#print("The square root of" ,rootsquare, "is approximately", square_root (rootsquare,approx))




    
