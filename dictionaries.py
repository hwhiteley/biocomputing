#Creating dictionaries and accessing elements

dict = {} #empty dictionary
base_names = {
    "A": "Adenine",
    "G": "Guanine",
    "T": "Thymine",
    "C": "Cystosine"
}
print(base_names["A"])
base_names.get("G") #accessing values through keys
for k in base_names: #accessing keys through a for loop
    print(k)

for key, value in base_names.items(): #printing both key and value
    print(key, value)

#access some data through a file and make a dictionary printed in ascending order - I did this my way (didn't copy the code)
d = {}
with open("C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\week2\\files_session4\\multi_seqs.txt", 'r') as f:
    for line in f:
        seq_identifer = line[0:5]
        d[seq_identifer] = len(line)
    sorted_d = sorted(d.items(), key=lambda x:x[1]) #here you use lambda to sort the dictionary by values, you don't need it if you
                                                    # sort by keys

print(sorted_d)

