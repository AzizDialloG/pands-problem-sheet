#Thierno Aziz Diallo
"""
Write a program that outputs whether or not today is a weekday.
An example of running this program on a Thursday is given below
"""
import datetime
#Monday is 0 and Sunday is 6

wdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] #using list 
today = today = datetime.datetime.today().weekday()
#print("Todays day is :", wdays[today]) #print today day ( i have edited this part) 

if today < 5: 

    print ("Yes, unfortunately today is a weekday.") #print if it is a week day
else: 
    print("It is the weekend, yay!") #print it is Weekend 
    pass
