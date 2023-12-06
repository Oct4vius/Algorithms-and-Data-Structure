import random

def is_sorted(list):
    for i in range(0, len(list) - 1):
        if list[i] > list[i+1]:
            return False
    return True 

def bongo_sort(list):
    while(not is_sorted(list)):
        random.shuffle(list)

    return list

l = []

for i in range(0,5):
    l.append(random.randint(0,100))

print(l)

print(bongo_sort(l))