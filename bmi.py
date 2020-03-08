#Thierno Aziz Diallo
#Calculate your body max index
'''
Write a program that calculates somebody's Body Mass Index (BMI).
This program calculates the person body mass index. 
The inputs are the person's weight in kilograms and height in centimeters.
The formula is:
BMI= (weight / (height ** 2)


'''
Height= float (input("Enter your Height in Centimeter:")) #enter the height in centimeter
Weight=float(input("Enter your Weight in Kilogram:")) # enter the weight in kilogram

BMI = Weight / ((Height / 100) ** 2) # BMI formula

print("Your Body Max Indix is",BMI) #Result of the body max index(BMI)
