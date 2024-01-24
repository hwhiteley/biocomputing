#Practical 4
#Use a range to print out numbers between 10 and 50 (no increment specified)

x = range(10,51)
for num in x:
    print(num)

#2. Amino-acid code conversion
#   Create a dictionary that maps 3-letter to 1-letter amino-acid codes using the file `aa_types.txt`. Use the dictionary
#   to convert the sequence in file `seq_3code.txt` to a simple sequence (single letter codes, no gaps).
#   Use the three letter aa code as a key and the one letter as the value
#   aa = {'ASN': 'N', 'ASP': 'D'...}
aa = {}
with open("C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\week2\\files_session4\\aa_types.txt", 'r') as f:
    for line in f:
        three_letter = line[0:3]
        aa[three_letter] = line[-2]
print(aa)


with open("C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\week2\\files_session4\\seq_3code.txt", 'r') as f2:
    for line in f2:
        content = f2.read().split() #seperating each amino acid

#use those amino acids as keys in the aa dictonary to get corresponding one letter aa.
values_for_seq3 = [aa[key] for key in content]
print(values_for_seq3)

#3. Set difference
#   Print out the number of species that are in file `species1.txt`, but not
#   in file `species2.txt`. And print out the number of species that are in
#   file `species2.txt` but not in file `species1.txt`. Consider using sets instead of dictionaries.
#   Thoughts on how to solve:
#        Convert each file into a set then use comparison operators to find unique elements to each set.


with open("C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\week2\\files_session4\\species1.txt", 'r') as file1:
    set_species1 = {line.strip() for line in file1}
print(set_species1)


with open("C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\week2\\files_session4\\species2.txt", 'r') as file2:
    set_species2 = {line.strip() for line in file2}
print(set_species2)

len(set_species1) #241
len(set_species2) #250

species_in_one_not_two = set_species1.difference(set_species2)
print(len(species_in_one_not_two)) #125

species_in_two_not_one = set_species2.difference(set_species1)
print(len(species_in_two_not_one)) #134


#More challenging
#**1. Intersection** NEED HELP FROM TRISTAN - FILES DON'T EXIST
# Each of the files named in file `filenames.txt` contains a list of words. Write a script that opens each of the files
# listed in file `filenames.txt`, reads in the words, and prints out (in no particular order) any words that occur in
# all of the files. Write the code so that it  will work if I add another file to `filenames.txt`.

#First how do you read files within a file

with open('C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\file_lists\\files.txt', 'r') as file_list_file:
    # Read the content of the file and split it into lines
    file_names = file_list_file.read().splitlines()
# Iterate through each file name and read its contents - NOT WORKING AS FILES PROVIDED DON'T EXIST
for file_name in file_names:
    with open(file_name, 'r') as file:
        content = file.read()

        # Process the content as needed
        print(f"Content of {file_name}:\n{content}\n")

#2. Amino-acid frequencies
# Count the number of each amino-acid type occurring within the
# sequence stored in file `seq_long.txt`. Print out a list of the amino
# acids and corresponding counts in descending order of frequency.
# create a dictionary with the aa as a key and the count as a value

with open('C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\week2\\files_session4\\seq_long.txt', 'r') as f:
    aminoacid = {} # create empty dictionary
    for line in f: #iterate through line
        for aa in line: #iterate through each amino acid in each line
            aminoacid[aa] = aminoacid.get(aa, 0) + 1 #set the aa as the key and get the count of that key

for aa, count in aminoacid.items():
    print(f"Character: {aa}, count = {count}")


#3. PDB codes and chain IDs
# A PDB chain ID consist of five characters (e.g. `1fb1A`): a 4-character
# identifier for a protein (here `1fb1`), and a one-character chain identifier
# (here `A`). Read in the 5-character PDB chain IDs from file
# `chain_ids.txt`

with open('C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\week2\\files_session4\\chain_ids.txt', 'r') as f:
    for line in f:
        print(line)
#
# Use a dictionary to store
# a) PDB codes (the keys) and
# b) a list of the single-character chain identifiers associated with
#    that PDB code (the values)
# Print them out in the following format, i.e.
# sorted alphabetically by PDB code and with chain letters also sorted:
# 1aoc: A B
# 1aoe: A B
# 1aof: A B
# 1b0c: A B C D E
# 1cij: A
# 1cik: A
# 1der: A B C D E F G H I J K L M N
# 1dfj: I
# 1dfk: A Y Z