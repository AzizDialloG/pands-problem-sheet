#Thierno Aziz Diallo
#Calculate your body max index
'''
Write a program that calculates somebody's Body Mass Index (BMI).
This program calculates the person body mass index. 
The inputs are the person's weight in kilograms and height in centimeters.
The formula is:
BMI= (weight / (height ** 2)


'''
#Getting input from the user and assigning it to user
height= float (input("Enter your Height in Centimeter:")) #enter the height in centimeter
weight=float(input("Enter your Weight in Kilogram:")) # enter the weight in kilogram

#Formula for calculating bmi
BMI = weight / ((height / 100) ** 2) # BMI formula

print("Your Body Max Indix is",BMI) #Result of the body max index(BMI)
