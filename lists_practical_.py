#Lists Practical
#List Operations example

#create a list from the numbers file:
numbers = []
with open('C:/Users/44785/Documents/Bioinformatics/biocomputing/files_session3/numbers.txt', 'r') as f:
    numbers = f.readlines()
numbers = [float(n) for n in numbers]

#apply numeric operators
print('Minimum:', min(numbers))
print('Maximum:', max(numbers))
print('Sum:', sum(numbers))

#Use enumerate and modify elements
#replace negative numbers with 0
print(enumerate(numbers))
for i, n in numbers:
    if n < 0:
        numbers[i] = 0
print(numbers)

# insert a star as middle element of list
middle_index = len(numbers) // 2
numbers.insert(middle_index, '*')
print(numbers)

# create a reverse copy of the list and add it to the end
reversed_numbers = list(reversed(numbers))
numbers = numbers + reversed_numbers
print(numbers)

#how many words are in both lists:
words1 = []
with open('C:/Users/44785/Documents/Bioinformatics/biocomputing/files_session3/words1.txt', 'r') as f:
    words1 = f.read().splitlines()

words2 = []
with open('C:/Users/44785/Documents/Bioinformatics/biocomputing/files_session3/words2.txt', 'r') as f2:
    words2 = f.read().splitlines()

# create a list containing words in both lists
# and print out its length
words_in_both = []
for w in words1:
    if w in words2:
        words_in_both.append(w)
print(len(words_in_both))

#print words exclusive to list2
words_2_exclusive = []

for w in words2:
    if w not in words1:
        words_2_exclusive.append(w)
print(words_2_exclusive)

#having an issue with the 'words' file - showing it will work with a local list
list1= [1,2,3]
list2 = [6,2,3]
exclusive_to_list2 = set(list2) - set(list1)
print(exclusive_to_list2)

#removing common words in both lists
for w in words2:
    if w in words1:
        words2.remove(w)


numbers = []
with open('C:/Users/44785/Documents/Bioinformatics/biocomputing/files_session3/integers.txt', 'r') as f:
    numbers = f.read().splitlines()

# There are two sorting alternatives:
# a) Here list itself is not sorted
print('Using sorted():\n', sorted(numbers))
# b) this time list is sorted
numbers.sort()
print('Using list.sort():\n', numbers)