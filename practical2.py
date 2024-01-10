#1. Pyhthagorous thereom
a^2 + b^2 = c^2
import math
def hypotenuse(a,b):
    c_squared = a**2 + b**2
    c = math.sqrt(c_squared)
    return c

print(hypotenuse(1,2))

#2 Alternate lines - open either way listed below. Also a way to open via Bash, later lectures
corvids_file = open('C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\week1\\corvids.txt', 'r')
for line in corvids_file:
    for line in corvids_file:
        print(line, end="")
corvids_file.close()

with open('C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\week1\\corvids.txt', 'r') as corvid_f:
    for line in corvid_f:
        print(line, end="")


#3 Modifying a for loop

total_numbers = 0
total_negative_numbers = 0
with open('C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\week1\\numbers.txt', 'r') as f:
    for line in f:
        total_numbers += 1
        if float(line) < 0:
            total_negative_numbers +=1


print('Total numbers:', total_numbers)
print('Total negative numbers:', total_negative_numbers)

#4 Write a for loop - script which counts and prints number of lines in file
total_lines = 0
with open('C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\week1\\numbers.txt', 'r') as f:
    for line in f:
        total_lines += 1
    print(total_lines)

