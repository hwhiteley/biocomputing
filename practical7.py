# Q1 loops and arithmetic
def add_sub(filename1, filename2):
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

print(add_sub("C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\week 4\\session7\\add.txt", "C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\week 4\\session7\\sub.txt" ))

# Q2 Birds and dictionaries

def bird_check(filename1,filename2,filename3):
    with open(filename1, 'r') as f:
        lines = f.readlines()
        birds_lst_1 = []
        for bird in lines:
            birds_lst_1.append(bird.upper())
    print(birds_lst_1)

    with open(filename2, 'r') as f2:
        lines = f2.readlines()
        birds_lst_2 = []
        for bird in lines:
            birds_lst_2.append(bird.upper())
    print(birds_lst_2)

    with open(filename3, 'r') as f3:
        lines = f3.readlines()
        birds_lst_3 = []
        for bird in lines:
            birds_lst_3.append(bird.upper())
    print(birds_lst_3)

    for bird in birds_lst_1:
        if bird in birds_lst_2 and birds_lst_3:
            print(bird)



bird_check("C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\week 4\\session7\\clever_birds.txt",
           "C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\week 4\\session7\\corvids.txt",
           "C:\\Users\\44785\\Documents\\Bioinformatics\\biocomputing\\week 4\\session7\\garden_birds.txt")