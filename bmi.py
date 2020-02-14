#Thierno Aziz Diallo
#Calculate your body max index
'''
Write a program that calculates somebody's Body Mass Index (BMI).This

'''
Height= float (input("Enter your Height in Centimeter:"))
Weight=float(input("Enter your Weight in Kilogram:"))

BMI = Weight / ((Height / 100) ** 2)

print("Your Body Max Indix is",BMI)
