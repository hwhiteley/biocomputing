# 1. Input from the keyboard
#
# Write a script that:
# Prints out the statement “Enter your name”:
# Reads in your name when you type in at the keyboard Prints out “My name is [your name]”.
user_input = input("Enter your name ")
print(f"My name is {user_input}.")

# B) Simple Arithmetic
# 1. Averages
# Write a script that calculates and prints out the average of two numbers read in from the keyboard.
# Write a second version of your script that calculates the average of 3 numbers read in from the keyboard.

number_input_a = int(input("Enter a number "))
number_input_b = int(input("Enter another number "))
avg = ((number_input_a+number_input_b)/2)
print(avg)

three_num = int(input("Enter 3 numbers to calculate average, seperated by commas"))
seperated_nums = three_num.split
print(seperated_nums)
avg_three_nums = sum(seperated_nums)/len(seperated_nums)
print(avg_three_nums)

def avg_three(n1,n2,n3):
    average = (n1+n2+n3)/3
    return average
print(avg_three(1,3,5))



#2. Area of square and cube
def square_calc(x):
    area = x*x
    volume = x**3
    return area, volume

print(square_calc(2))

#Circumference and area of a circle
import math
def circle_calc(x): #where x is the diameter
    r = x/2
    area = math.pi*(r**2)
    circum = 2*(math.pi)*r
    return area, circum
print(circle_calc(10))

#Ancestor q
def ancestor(x):
    gen= 2024 - int(x)
    num_ancestors = gen/25
    return num_ancestors

print(ancestor(1999))

#time convertor seconds into days, hours, minutes
sec_day = 60*60*24 #8640
sec_hour = 60*60 #360
sec_min = 60 #60

from datetime import datetime, timedelta

def GetTime(s):
    sec = timedelta(seconds=int(input('Enter the number of seconds: ')))
    d = datetime(1,1,1) + sec

    print("DAYS:HOURS:MIN:SEC")
    print("%d:%d:%d:%d" % (d.day-1, d.hour, d.minute, d.second))
GetTime(3600)

#circle in rectangle area
def area(a):
    area_rect = (2*a) * a
    r = a//2
    area_circ = math.pi*(r**2)
    shaded_area = ((area_rect//2)-area_circ)
    return shaded_area

print(area(1))
