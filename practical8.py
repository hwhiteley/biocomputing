import numpy as np
import re
import matplotlib.pyplot as plt

def f_measure(tp, fp, fn):
    '''
    :param tp: true positive value, integer
    :type tp: int
    :param fp: false positive value, integer
    :type fp: int
    :param fn: false negative value, integer
    :type: fn: int
    :return: returning the F-score, a measure of predictive performance
    '''

    if tp < 0 or fp < 0 or fn < 0:
        raise ValueError("tp, fp, and fn must be non-negative integers")
    try:
        F1 = (2 * tp) / ((2 * tp) + fp + fn)
    except ZeroDivisionError:
        raise ValueError("You can't divide by zero, try another value for tp")

    return F1


def mcc_classification(tp, tn, fp, fn):
    try:
        CC = ((tp * tn) - (fp * fn)) / np.sqrt((tp + fp)*(tp + fn)*(tn + fp)*(tn + fn))
    except ValueError:
        print("You can't divide by zero.")
        CC = None
    return CC


# Create a pie chart from the data in file `pdb_counts.txt` showing the
# distribution of released structures in the Protein Data Bank by organism
# (excluding entries from a non-natural source). Here are the contents of the file:

def pie_chart_from_txt(file):
    with open(file, 'r') as data:
        text = data.read()

        # create a dictionary from the text file to use in the pie chart
        organism_dict = {}
        for line in text.strip().split('\n'):
            # Split each line into organism name and count based on the colon
            organism, count = line.split(':')
            # Remove leading and trailing whitespace from organism name
            organism = organism.strip()
            # Convert count to integer
            count = int(count.strip())
            # Add entry to the dictionary
            organism_dict[organism] = count

    organism_names = list(organism_dict.keys())
    counts = list(organism_dict.values())
    # to use in the next for loop
    total_counts = (sum(counts))
    counts_list = []
    for organism, count in organism_dict.items():
        percentage = round((count / total_counts) * 100, 2)
        counts_list.append((percentage, organism))

    # Create the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(counts, labels=organism_names, autopct='%1.1f%%')
    plt.title('Organism Distribution\n')

    # Show the plot
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

    return counts_list


print(pie_chart_from_txt("C:/Users/44785/Documents/Bioinformatics/biocomputing/Files for session 8-20240227/pdb_counts.txt"))

