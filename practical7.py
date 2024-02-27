import matplotlib.pyplot as plt
import numpy as np
import json
import re
from scipy.stats import laplace

# Q1 loops and arithmetic
def add_sub(filename1, filename2):
    ''''''
    with open(filename1, 'r') as f:
        lines = f.readlines()
        numbers_add = 0
        for num in lines:
            numbers_add += int(num)
    print(numbers_add)
    with open(filename2, 'r') as f:
        lines = f.readlines()
        numbers_sub = 0
        for num in lines:
            numbers_sub -= int(num)
    print(numbers_sub)

    return numbers_add + numbers_sub

# print(add_sub("C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\week 4\\session7\\add.txt", "C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\week 4\\session7\\sub.txt" ))

# Q2 Birds and dictionaries - Which single bird species is a garden bird (file garden_birds.txt), a member of the family
# Corvidae (file corvids.txt), and clever (file clever_birds.txt)? Beware differences in the way uppercase and lowercase
# is used in the files.

def bird_check(filename1,filename2,filename3):
    '''

    :param filename1: txt file
    :param filename2: txt file
    :param filename3: txt file
    :return: Returning the bird species common to all files in a list format
    '''
    with open(filename1, 'r') as f:
        lines = f.readlines()
        # initialize empty list for first bird file
        birds_lst_1 = []
        for bird in lines:
            # appending all birds to this list, in upper case (will do the same for all chars in further lists)
            birds_lst_1.append(bird.upper())


    with open(filename2, 'r') as f2:
        lines = f2.readlines()
        # initialize empty list for second bird file
        birds_lst_2 = []
        for bird in lines:
            birds_lst_2.append(bird.upper())


    with open(filename3, 'r') as f3:
        lines = f3.readlines()
        # initialize list for third bird file
        birds_lst_3 = []
        for bird in lines:
            birds_lst_3.append(bird.upper())

    # use a for loop to compare birds in all lists and add those to a new list if the bird appears in all three
    common_birds = []
    for bird in birds_lst_1:
        if bird in birds_lst_2 and birds_lst_3:
            common_birds.append(bird)

    stripped_list = [s.strip() for s in common_birds]

    birds_json = json.dumps(stripped_list, indent=4) #changing the format to json - just to see

    return birds_json


#
# print(bird_check("C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\week 4\\session7\\clever_birds.txt",
#            "C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\week 4\\session7\\corvids.txt",
#            "C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\week 4\\session7\\garden_birds.txt"))

# **3. Regexes and PDB files**
#
# Extract the (scientific) species and strain names from PDB header files `12e8.h` and print them out in lowercase. To
# find the species and strain names, you need to find the labels `ORGANISM_SCIENTIFIC` and `STRAIN` respectively. Can
# you generalize your script so that it will read in all files with the extension `.h` in the current working directory
# and print out the same information for each file? (Two potential approaches were covered in session 7, section 1.)

def species_strain_names(file):
    with open(file, 'r') as file:
        file_content = file.read()
        # use a regex to obtain text after specified words, STRAIN and ORGANISM_SCIENTIFIC
        pattern_strain = r'STRAIN:\s*(.*?)\s*;'
        pattern_organism_scientific = r'ORGANISM_SCIENTIFIC:\s*(.*?)\s*;'

        # Use re.search() to find the first match in the source string
        strain_match = re.search(pattern_strain, file_content)
        organism_match = re.search(pattern_organism_scientific, file_content)

        strain_info = strain_match.group(1) if strain_match else None
        organism_info = organism_match.group(1) if organism_match else None

        return strain_info, organism_info



## Numbers and Plots
#
# **1. Shuffling**
#
# Create a NumPy array of 8 integers using the arange function. Write a
# Python script that calculates how many times you have to shuffle the
# array before (by chance) you get the original ordering of integers back.

a = np.arange(0, 8)
b = a.copy()

counter = 0
while True:
    np.random.shuffle(a)
    counter += 1

    if np.array_equal(a, b):
        print('Found: ', counter)
        break

# **2. Comparing distributions**
#
# Write a script that plots two sets (*A* and *B*) of dots – each set should
# contain the same number of dots, but of different colours. The *x,y*
# # coordinates of set *A* should be from a normal distribution, and those of
# # set *B* from a Laplace distribution. Run the script several times with a
# # different number of dots. To what extent can you see the differences
# # between the two distributions in these plots? (This is a qualitative
# # judgement about what you are seeing &mdash; there is no definitive answer!)
# #
# # **Hint:** You can invoke the relevant functions as follows:<br>
# # `norm_x = np.random.normal(size=n_dots, s=1)`<br>
# # `lap_x = np.random.laplace(size=n_dots, s=1)`<br>
# # Here `s=1` ensure the dots are very small.
#
# n = 1000
# # normal distribution
# x_norm = np.random.normal(size=n)
# y_norm = np.random.normal(size=n)
# plt.scatter(x_norm, y_norm, c= 'b', alpha=0.1,  s=10) # alpha controls transparency of the dots
#
# # laplace distribution
# x_lap = np.random.laplace(size=n)
# y_lap = np.random.laplace(size=n)
# plt.scatter(x_lap, y_lap, c= 'r', alpha=0.1, marker='x', s=10)

# plt.show()

# **3. Plot curves from file**
# There are four columns of data in file `plot_data.txt`. Plot four curves, one per column. Treat the numbers in a given
# column as the *y*-axis values for the curve. Generate your own set of values for the *x*-axis using `arange` (this
# should be the same for each curve). Make sure every curve is a different colour.


# Read data from file
# data = np.loadtxt('plot_data.txt')
#
# # Generate x-axis values
# x = np.arange(len(data))
#
# # Plot each column as a separate curve
# for i in range(data.shape[1]):
#     plt.plot(x, data[:, i], label=f'Curve {i+1}', color=plt.cm.viridis(i / data.shape[1]))
#
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Four Curves from plot_data.txt')
# plt.legend()
# # plt.show()

# An important part of programming is to learn how to work out the solution to a problem using techniques that are
# completely new to you. In that spirit: create a plot consisting of a sine wave (in black) that has alternate peaks and
# troughs filled in (solid) red. No hints!
#
# If that’s too easy, add axis ticks and labels.

fs = 100 # sample rate
f = 2 # the frequency of the signal

x = np.arange(fs) # the points on the x axis for plotting
# compute the value (amplitude) of the sin wave at the for each sample
y = np.sin(2*np.pi*f * (x/fs))


# showing the exact location of the smaples
plt.stem(x,y, 'r', )
plt.plot(x,y)
plt.show()

