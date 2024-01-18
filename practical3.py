#read in numbers from 'numbers.txt' file and print them out in reversed order

with open('C://Users//44785//Documents//Bioinformatics//biocomputing//files_session3//numbers.txt', 'r') as file:
    result = file.read().splitlines()
print(result[::-1])

#bio sequence length. Print out the total length of the protein, that is the total of three letter amino acids!
#split into lines, count iterations of 3 multiply by total lines
#split file into individul elements then find the length of new list
with open('C://Users//44785//Documents//Bioinformatics//biocomputing//files_session3//seq_3code.txt', 'r') as file:
    result = file.read()
    print(result)

split_list = result.split()
num_proteins = len(split_list)//3
print(f"Number of proteins: {num_proteins}")

#Count the length of each protein sequence, secondary structure in DSSP is written underneath
with open('C://Users//44785//Documents//Bioinformatics//biocomputing//files_session3//seq_ss_n.txt', 'r') as file:
    result = file.read()

split = result.split()
print(split)

for x in split:
    if len(x) >= 47:
        print(f" This protein: {x} is {len(x)} amino acids long.")

# second question is the same as one above as I didn't have the file without n at the start of each line.
# could use the same function though ^

# Something a bit more challenging..........
# Pick an amino acid, write code to calculate the percentage of that amino acid in a protein from the same file as above
# I will choose A - alanine
print(result) # still have the file open
# i will use the code from previous answer

for element in split:
    letters_found = [char for char in element if char== 'A']
    print(f'Letters in "{element}": {letters_found}')
    total_characters = len(element)
    if total_characters > 0:
        percentage_letters = (len(letters_found) / total_characters) * 100
    else:
        percentage_letters = 0
    print(f'Percentage of letters in "{element}": {percentage_letters:.2f}%\n')

# Palindrome
#couldn't import file so I will skip but here is code to find a palindrome

with open() as text:
    for line in text:
        line = line.strip()
        line2 = line[::-1]
        if line == line2:
            print ('Palindrome!')

# Optional challenge: a 'real' problem
# A colleague comes and ask you whether you can identify *all* the peptide fragments. In other words, every possible
# pair of sub-sequences, with each pair containing exactly one cysteine, symbol `C`. Additionally, your colleague
# would like to restrict this to fragments that can be obtained by trypsin digestion, that is, peptide fragments that
# have been split just before the occurence of a lysine symbol `K``.

albumin_sequence = "MKWVTFISLLFLFSSAYSRGVFRRDAHKSEVAHRFKDLGEENFKALVLIAFAQYLQQCPFEDHVKLVNEVTEFAKTCVADESAENCDKSLHTLFGDKLCTVATLRETYGEMADCCAKQEPERNECFLQHKDDNPNLPRLVRPEVDVMCTAFHDNEETFLKKYLYEIARRHPYFYAPELLFFAKRYKAAFTECCQAADKAACLLPKLDELRDEGKASSAKQRLKCASLQKFGERAFKAWAVARLSQRFPKAEFAEVSKLVTDLTKVHTECCHGDLLECADDRADLAKYICENQDSISSKLKECCEKPLLEKSHCIAEVENDEMPADLPSLAADFVESKDVCKNYAEAKDVFLGMFLYEYARRHPDYSVVLLLRLAKTYETTLEKCCAAADPHECYAKVFDEFKPLVEEPQNLIKQNCELFEQLGEYKFQNALLVRYTKKVPQVSTPTLVEVSRNLGKVGSKCCKHPEAKRMPCAEDYLSVVLNQLCVLHEKTPVSDRVTKCCTESLVNRRPCFSALEVDETYVPKEFNAETFTFHADICTLSEKERQIKKQTALVELVKHKPKATKEQLKAVMDDFAAFVEKCCKADDKETCFAEEGKKLVAASQAALGL"