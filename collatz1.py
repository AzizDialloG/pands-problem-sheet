#Thierno Aziz Diallo
#Week 4
#Task 4
"""
This program will ask user to input any positive value (integer)
And output the successive values of the folling calculation.
At each step calculate the next value by taking the current value and 
if it's even, devide it by 2, but it's odd, multiply it by three and add one.
"""

a = int(input("Enter any positive integer number: "))

while a != 1:
#when devided by 2 is even
#a/2
    if int(a) % 2 == 0:
      a = int(a)/2
      
#when a is odd multiply by 2 then add 1
    else:
      a = int(a)*3+1
    print (a)

print ("end")  
