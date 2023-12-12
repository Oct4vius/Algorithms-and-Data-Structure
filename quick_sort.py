import random

"""
Time complexity 
best case O(n log n)
worst case O(n↑2)
"""

def quick_sort(values):
    if len(values) <= 1:
        return values
    
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


l = []
for i in range(0,5):
    l.append(random.randint(0,100))
print(l)
sorted_number = quick_sort(l)
print(sorted_number)