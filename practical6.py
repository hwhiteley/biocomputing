#Practical 6
# Q1
# Printing a range 0,100 in increments of 5
for num in range(0,105,5):
    print(num)


# Q2
# This code should read a file, attempt to find a motif in it, then print its position, as well as 10 characters on each
# side
# -APPROACH func with motif_finder(filename,motif). Iterate through the lines, check for motif in line. If motif found
#  make a variable storing the index for the motif - will be the first letter in motif.
#  then make two variables with -10 and +12 to the index to get ten chars either side respectively

def motif_finder(filename,motif):
    with open(filename, 'r') as f:
        lines = f.readlines()
        motif_results = []
        for line in lines:
            # print(line)
            if motif in line:
                result = line.index(motif)
                # print("Motif found in this line!", line)
                # print("Index of the motif:", result)
                index_plus_ten = result + 12
                index_minus_ten = result - 10
                motif_results.append(line[index_minus_ten:index_plus_ten])
        return motif_results

# print(motif_finder("C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\week3\\Files for session 6-20240126\\seq_long.txt", 'GG'))

# Q3 This code should read an alignment from a file, then output the last 10 characters in the alignment

from Bio.Seq import Seq
from Bio import AlignIO

# filename = "C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\week3\\Files for session 6-20240126\\hAPP.phylip"
# alignment = AlignIO.read(filename, 'phylip')
# print(alignment)

def last_ten_alignment(file):
    alignment = AlignIO.read(file, 'clustal')
    return alignment[:,-10:]
print(last_ten_alignment("C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\week3\\Files for session 5-20240122\\hAPP.clustal"))
