#Thierno Aziz Diallo
#TASK3
'''Write a program that takes asks a user to input a string and outputs every second letter in reverse order. '''
#This program prints each second string character, it starts by the last one.

firststr = str(input("Type a string: "))
size = (len(firststr)) # counts the number of character on the string.
print(firststr[-1:-size:-2]) #prints each second character by starting with the last one.
