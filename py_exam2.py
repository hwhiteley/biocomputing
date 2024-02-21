from Bio.Seq import Seq
import statistics
import matplotlib.pyplot as plt

def generate_number_list():
    """Question 1
        Return a sequence comprising the following sequence of numbers: `3 6 9 12 15 18 21`.

        Example use: generate_number_list()
        Example output: 3 6 9 12 15 18 21
    """
    # Complete the function body below to answer question 1
    my_sequence = Seq('3 6 9 12 15 18 21') # simply return a sequence object containing the numbers specified
    return my_sequence


def lex_sort_file(filename):
    """Question 2
        The file with the filename given as an argument contains several amino-acid sequences, one per line.
        Write a function that returns lines in a sequence, sorted in lexicographical order.

        Example use: lex_sort_file()
        Example output:
        ['AALKIDSTVSQDSAWYTATAINKAGRDTTRCKVNVEVEFAEPEPERKLIIPRGTYRAK',
         'AEKTAVTKVVVAADKAKEQELKSRTKEVITTKQEQMHVTHEQIRKETEKTFVPKVV',
         'EAVATGAKEVKQDADKSAAVATVVAAVDMARVREPVISAVEQTAQRTTTTAVHIQPAQEQVRKE',
         'EGRKGLQRIEELERMAHEGALTGVTTDQKEKQKPDIVLYPEPVRVLEGETARF',
         ...
    """
    # Complete the function body below to answer question 2
    with open(filename, 'r') as f:
        lines = f.readlines()  #read the lines
    cleaned_lines = [line.rstrip('\n') for line in lines] #remove the new line char
    sorted_lines = sorted(cleaned_lines) #sort into lexi order

    return sorted_lines


def top_lysine_stats(filename):
    """Question 3
        Work out which sequence from file `multi_seqs.txt` has the highest percentage of lysine (`K`) residues,
        and return out both the percentage and the sequence.

        Example use: top_lysine_stats()
        Example output:  17.86, AEKTAVTKVVVAADKAKEQELKSRTKEVITTKQEQMHVTHEQIRKETEKTFVPKVV

    """
    # Complete the function body below to answer question 3
    with open(filename, 'r') as f:
        lines = f.readlines()  #read the lines
    cleaned_lines = [line.rstrip('\n') for line in lines] #remove the new line char same as func above to get the seq
    residue_percentage = {} # initialise an empty dict
    for line in cleaned_lines: #iterate through the lines in the file
        total_residues = len(line)
        residue_count = line.count('K')
        percent = (residue_count / total_residues) * 100 #calculate the percentage of residue

        residue_percentage[line] = percent # then add the sequence as a key and the perentage as the value

    max_sequence = max(residue_percentage, key=residue_percentage.get)
    max_percent = residue_percentage[max_sequence]
    return max_percent, max_sequence


def avg_lysine_stats(filename):
    """Question 4
        Compute the mean and median number of lysines in sequences in `multi_seqs.txt`, and return them

        Example use: avg_lysine_stats()
        Example output:  (4.390243902439025, 4.0)
    """
    # Complete the function body below to answer question 4
    with open(filename, 'r') as f:
        lines = f.readlines()  #read the lines
    cleaned_lines = [line.rstrip('\n') for line in lines]
    mean_counts = []
    residues = [] # initialise an empty list which will be used for median calculation
    for line in cleaned_lines: #iterate through the lines in the file
        residues_count = (line.count('K'))
        residues.append(int(residues_count)) #append the number of K residues to the list
        mean = (sum(residues) / len(cleaned_lines)) #calculate the percentage of residue
        mean_counts.append(mean)
    median = (statistics.median(residues))
    return mean, median


def plot_lysine_stats (filename="multi_seqs.txt"):
    """Question 5
        Wrte a function that plot the distribution of lysine counts, in the sequences from file `multi_seqs.txt`.

        Example use: plot_lysine_stats()
        Example output:  <plot of the lysine count distribution>
    """
    # Complete the function body below to answer question 5
    # Just expanding previous answers to plot

    with open(filename, 'r') as f:
        lines = f.readlines()  # read the lines

    cleaned_lines = [line.rstrip('\n') for line in lines]
    residues = []  # initialize an empty list which will be used for median calculation

    for i, line in enumerate(cleaned_lines, start=1):  # iterate through the lines in the file with sequence numbers
        total_residues = len(line)
        residues_count = line.count('K')
        residues.append(int(residues_count))  # append the number of K residues to the list

    mean = sum(residues) / len(cleaned_lines)  # calculate the mean
    median = statistics.median(residues)  # calculate the median

    # Plotting
    plt.plot(range(1, len(cleaned_lines) + 1), residues, marker='o')
    plt.title('Lysine Count in Sequences')
    plt.xlabel('Sequence Number')
    plt.ylabel('Lysine Count')
    plt.show()

    return


def translate_dna(codons, dna):
    """Question 6
    File `codons.txt` includes a non-standard codon table, including start and stop codons. Use the codons in that file to translate the DNA sequence in `dna.txt` into multiple protein sequences.
    To do this, you need to:
- Scan the DNA sequence (from its start), until you find a *start codon*
- Translate the codons one at a time until you encounter a *stop codon*
- Continue scanning the DNA sequence until you find the next *start codon*, and so on.

*Note 1:* Ignore the possibilty of different reading frames, i.e. assume the first codon consists of the first 3 letters in the sequence, and so on.

*Note 2:* Do not use Biopython to answer this question!

Here is a **simple example**:

DNA sequence: `CGTATGGGTTCGATGTCGGTCTAACCC`

`CGT` &mdash; not a *start codon*, so skip it<br>
`ATG` &mdash; *start codon*<br>
`GGT` &mdash; translate to G<br>
`TCG` &mdash; translate to S<br>
`ATG` &mdash; translate to M (identical to *start codon*, but we have already started)<br>
`TCG` &mdash; translate to S<br>
`GTC` &mdash; translate to V<br>
`TAA` &mdash; *stop codon*<br>
`CCC` &mdash; not a *start codon*, so skip it<br>

So for this DNA sequence, the peptide sequence `GSMSV` should be returned.

        Example use: translate_dna()
        Example output:  ['YTSRRSPSSVGF', ...]
    """
    # Complete the function body below to answer question 6
    # make a dictionary with the codon table
    with open(codons, "r") as codon_table:
        lines = codon_table.readlines()
        amino_acids_dict = {}

        # Parse the data and populate the dictionary
        for entry in lines:
            parts = entry.split(':')
            amino_acid = parts[0].strip()
            codon = parts[1].strip().split()
            amino_acids_dict[amino_acid] = codon

    # Make a for loop to check every three index values to the dictionary values and return the corresponding key
    with open(dna, "r") as dna_file:
        lines = dna_file.readlines()
        new_list = []  # empty new list which will contain the three codons from dna file
        for string in lines:
            codons = [string[i:i + 3] for i in range(0, len(string), 3)]  # Create codons of three characters
            new_list.extend(codons)  # add the codons into the new list

    translated_sequence = []

    # Iterate through the codons and find the corresponding amino acid
    for codon in new_list:
        # print(codon)
        for amino_acid, codon_list in amino_acids_dict.items():
            if codon in codon_list:
                translated_sequence.append(amino_acid)
                # print(translated_sequence)

    return translated_sequence[5::]


def longest_translatable_sequence(codons_fname='../data/codons.txt', dna_fname='../data/dna.txt') -> int:
    """Question 7
    Find and return the length of the longest translatable sequence in `dna.txt`:
    - the sequence starts with a start codon
    - the sequence ends with a stop codon
    - both start and stop codons should be in the same reading frame
    - there cannot be a stop codon in the same reading frame within the sequence
    - consider all three reading frames

    N.B.: Attempt this question last!

            Example use: longest_translatable_sequence()
            Example output:  245
    """
    # Complete the function body below to answer question 7






    return
