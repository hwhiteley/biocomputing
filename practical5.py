from Bio.Seq import Seq
from Bio.Seq import MutableSeq

random_seq = 'agggcctatagctcaacagcgggggcaaa'
dna = Seq(random_seq)
print("DNA sequence:", dna)
print("First four nucleotides in the sequence: ", dna[0:4])
print("GG count:", dna.count('gg'), '\n')
#you can slice the sequence then add that sub sequence onto the original
sub_seq = dna[15:]
print("Sub sequence:", sub_seq)
dna = dna + sub_seq
print("Revised sequence (original and sliced):", dna)
print("Length of new dna:", len(dna), '\n')
#printing the seq in upper
print("DNA sequence:", dna.upper())
print("Complement sequence:", dna.complement().upper())
print("Reverse complement: ", dna.reverse_complement().upper())

#Sequences in Bio.Seq are immutable but you can transfrom seq into an immutable list by doing the following:
mutable_seq = MutableSeq(str(dna)) #ensure you have imported MutableSeq from Bio.Seq
print(type(mutable_seq)) #class 'Bio.Seq.MutableSeq'
mutable_seq.reverse()
print("Reversed:", mutable_seq)
mutable_seq[1] = 'g' #mutating the sequence
print("Mutated sequence:", mutable_seq)

#Transcription and Translation

mrna = dna.transcribe()
print("Original dna:", dna)
print("MRNA sequence:", mrna)
print("Reverse transcription:", mrna.back_transcribe())

#Now we transcribe the MRNA into protein this can cause errors - biological errors. The MRNA sequence is not a multiple
#of 3, therefore we have a partial codon at the end of the sequence - python warns when you try and run the code
prot = mrna.translate()
print("Default protein sequence:", prot)
print("DNA sequence directly into protein:", dna.translate())
print(43//3)
print("Protein length", len(prot),'\n')

#mitochondrial protein alphabet - .alphabet is not a function ?????
mitochondrial_prot = mrna.translate(table="Vertebrate Mitochondrial")
protein_alphabet = set(str(mitochondrial_prot))
print('Mitochondrial protein sequence:', mitochondrial_prot)
print('Mitochondrial protein alphabet:', protein_alphabet)

#Checking for mystery protein
mystery_dna = 'aaccgttgtagagttgtt'
target_protein = 'NNSTTV'

this_dna = Seq(mystery_dna) #convert the string into a sequence
print("DNA sequence:", this_dna)
print("Complement:", this_dna.complement())
print("Reverse complement:", this_dna.reverse_complement())
mystery_protein = this_dna.translate() #this will translate that sequence into the proteins
print("Mystery protein:", mystery_protein)

if mystery_protein == target_protein:
    print("Protein match!")
else:
    mystery_rc = this_dna.reverse_complement() #reverse complement of the dna sequence
    print("DNA reverse complement:", mystery_rc)
    mystery_prot_reversed = mystery_rc.translate()
    print("DNA translated reversed:", mystery_prot_reversed)
    if mystery_prot_reversed == target_protein:
        print("Found Reverse!")
    else:
        print("Not found")

# Are these two DNA sequences the same? When translated using the Standard Code, do they produce **the same protein
# sequence**? Write a script that:
# - Prints out `The same DNA`, if the DNA sequences are the same
# - Prints out `The same protein`, if the DNA sequences are different but the protein sequences are the same
# - Prints out `Different` if the protein sequences don't match.

from Bio.Seq import Seq

def compare_dna_protein_sequences(dna_seq1, dna_seq2):
    # Create Seq objects for the DNA sequences
    seq1 = Seq(dna_seq1)
    seq2 = Seq(dna_seq2)

    # Check if the DNA sequences are the same
    if seq1 == seq2:
        print('The same DNA')
        return

    # Translate the DNA sequences into protein sequences
    protein_seq1 = seq1.translate()
    protein_seq2 = seq2.translate()

    # Check if the protein sequences are the same
    if protein_seq1 == protein_seq2:
        print('The same protein')
    else:
        print('Different')


dna1 = Seq('aaccgttgtagagttgttaaccgttgtagagttgtt')
dna2 = Seq('AACCGTTGTAGAGTTGTCAACCGTTGTAGAGTTGTT')
compare_dna_protein_sequences(dna1, dna2)

#Sequence alignments

from Bio import AlignIO
alignment = AlignIO.read("C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\week3\\Files for session 5-20240122\hAPP.clustal", 'clustal')
print(alignment)
print(type(alignment)) #<class 'Bio.Align.MultipleSeqAlignment'>
print(alignment[:2]) #selecting first two rows
print(alignment[:,:10]) #prints the first ten columns of all rows