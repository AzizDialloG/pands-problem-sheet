# pands-problem-sheet
# Thierno Aziz Diallo
# Programming and Scripts
The repository contains all exercises for this module, from week 2 to week 8.

# Requirements
In Order to run weekly tasks, the Python interpreter must be installed on the local computer.
Some one of the weekly task need some requirements, as installing numpy console and matplotlib.
# Scripts by weekly tasks

# Weekly task 2

Write a program that calculates somebody's Body Mass Index (BMI). The inputs are the person's height in centimetres and weight in kilograms. The output is their weight divided by their height in metres squared.

$ python bmi.py
Enter weight: 65
Enter height: 180
BMI is 20.06.
# Solution
This program calculates the person body mass index. 
The inputs are the person's weight in kilograms and height in centimeters.
The formula is:
BMI= (weight / (height ** 2)
# Sources
https://www.thecalculatorsite.com/articles/health/bmi-formula-for-bmi-calculations.php


--------
# Weekly 3 task

 Write a program that takes asks a user to input a string and outputs every second letter in reverse order.

$ python secondstring.py
Please enter a sentence: The quick brown fox jumps over the lazy dog.
.o zletrv pu o wr cu h
# Solution 
This program prints each second string character, it starts by the last one.
The simplest way is to use the built in function, len() by following the week 3 videos that were posting by the teacher and book recommended 
# Sources 
Recommended reading
Up to page 9 of A Whirlwind Tour of Python by Jake Vanderplas.

---------------------------------
# Weekly 4 task

Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

$ python collatz.py
Please enter a positive integer: 10
10 5 16 8 4 2 1
# Solution
Take any natural number n.
If n is even, divide it by 2.
 If n is odd multiply it by 3 and add 1.
 Repeat the process indefinitely.
 # Sources:
 https://www.w3schools.com/python/python_while_loops.asp
 Online videos by the Teacher 
 
 -----------------------------
#  Weekly task 5

Write a program that outputs whether or not today is a weekday. An example of running this program on a Thursday is given below.

$ python weekday.py
Yes, unfortunately today is a weekday.

An example of running it on a Saturday is as follows.

$ python weekday.py
It is the weekend, yay!
# Solution
I used list and if statements for this program
# Sources:
Week 5 online tutorial and some online resources 
Recommended reading
Read Real Python's blog posts on List and Tuples and Dictionaries.
https://pythontic.com/datetime/date/weekday
https://www.w3schools.com/python/python_conditions.asp
--------------------------------------
# Weekly task 6
#Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
#You should create a function called sqrt that does this.
"""
$ python squareroot.py
Please enter a positive number: 14.5
The square root of 14.5 is approx. 3.8
# Solution
I used the Newtown's method, the program takes a positive floating point num as an input and outputs an approximation of its square root.
# Sources:
Week 6 online tutorial and some online resources 
http://danielhomola.com/2016/02/09/newtons-method-with-10-lines-of-python/
https://www.youtube.com/playlist?list=PL3DE5C8688C5E7CAF
----------------------
# Weekly task 7
Write a program that reads in a text file and outputs the number of e's it contains.
The program should take the filename from an argument on the command line
$ python read_a_text_file.py 
# Solution
This program outputs the number of e's it contains.
# Requirement:
The file must be in the same folder.
# Sources:
Week 7 online tutorial and some online resources 
http://ccat.sas.upenn.edu/gopher/text/fiction/MobyDick/
https://www.datacamp.com/projects
----------------------------------
# Weekly task 8
Write a program that displays a plot of the functions 
f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
$ chart.py
# Solution
The program plots a chart on the screen based on f(x)=x, g(x)=x2 and h(x)=x3.
# Requirements:
To fully run this program, we will need to install numpy and matplolib.
If numpy and matplotlib are not imported will get :
    ModuleNotFoundError: No module name 'numpy'
    ModuleNotFoundError: No module name 'matplotlib'
# Sources:
Week 8 online tutorial and some online resources 
https://www.mathworks.com/help/matlab/ref/fplot.html
https://matplotlib.org/tutorials/introductory/pyplot.html
https://matplotlib.org/api/pyplot_api.html
https://stackoverflow.com/questions/38666527/what-is-the-necessity-of-plt-figure-in-matplotlib
https://scipy-lectures.org/intro/matplotlib/index.html





