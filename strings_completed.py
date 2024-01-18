#Strings

s = 'ILE TRP GLU LEU LYS LYS ASP VAL'

# Count the number of occurences of LYS (lysine)
print('Number of lysines:', s.count('LYS'))

# Count the number of amino acids in the string
aa_list = s.split()
print('Total number of amino acids:', len(aa_list))


#revert the og string

aa_list = ' '.join(s)
print(aa_list)

#species file

lines = []
with open("C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\files_session3\\pdb_species.txt", 'r') as f:
    lines = f.read().splitlines()
print(lines)

all_species = []
for s in lines:
    print(s) #prints the whole line - pdb identity + species
    species = s[11:] #slice the line so you only print from index 11 to the end
    print(species)
    all_species.append(species) # append this species name to a new list, all_species
print(all_species)

#extend this script so that it prints numbers with 1 decimal place


numbers = []
with open("C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\files_session3\\numbers.txt", 'r') as f:
    numbers = f.read().splitlines()
print(numbers)

# The code below would work if the values in the list were ints - they're strings here though
# rounded_numbers = [round(num, 1) for num in numbers]
# for rounded_num in rounded_numbers:
#     print(rounded_num)

#So you do it this way...
for num in numbers:
    num = float(num)
    rounded_num = round(num, 1) # rounded the numbers in the list to 1 dp
    print(f"{rounded_num:9.1f}") #aliging by using 8.1 - 9 indexes from the left and still keeping 1 dp.


#using these two strings output - 'SESSION A', 'SESSION B', 'SESSION C'
prefix = 'Session'
session_labels = 'ABCDEFG'

for letter in session_labels:
    print(f"{prefix.upper()} {letter}")

# two sequences - calculate the % of similarity. ie calculate the amount of times, in a percent where the two indexes
# align :)
# thoughts: iterate through each list and compare each index value to each other - if they match + 1 to a counter.
# finally counter/len(list)*100
# print percentage

seq1 = 'ACWQTEDGSSAKLCRYIPRMTASWFSERAHIKLTYRV'
seq2 = 'ACWQTFDGDSAKLCRYIRRMTASWFSFRAHIKIYYRV'
lst_seq1 = []
for letter in seq1:
    lst_seq1.append(letter)

lst_seq2 =[]
for letter in seq2:
    lst_seq2.append(letter)

len(lst_seq1)
len(lst_seq2)

#** Why doesn't this loop work below.... iterating through each list and comparing...

i = 0
j = 0
counter = 0
for i in range(len(lst_seq1)):
    for j in range(len(lst_seq2)):#both lists are the same length
        for value in lst_seq1:
            if value[i] == lst_seq2[j]:
                counter += 1
            i += 1
        j += 1
print(counter//len(seq1)*100)

# The way below worked
# Ensure both strings are of the same length
if len(lst_seq1) != len(lst_seq1):
    raise ValueError("Both strings must be of the same length.")

# Calculate the percentage of characters that are the same at the same index
percentage_same = sum(x == y for x, y in zip(lst_seq1, lst_seq2)) / len(lst_seq1) * 100

# Print the result
print(f"Percentage of characters that are the same: {percentage_same:.2f}%")

#The way Tristan did it below

same_aa_count = 0
if len(seq1) == len(seq2):
    for i, aa in enumerate(seq1):
        if aa == seq2[i]:
            same_aa_count += 1
    print('Sequence identity (%) =', (same_aa_count / len(seq1)) * 100)
else:
    print('Sequences are not the same length')








