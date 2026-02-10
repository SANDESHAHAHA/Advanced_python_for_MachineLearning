#12. Write a Python program to find the largest and smallest numbers in a list.

def find_max_min(lst):
    m,l= max(lst),min(lst)
    return m,l
numbers=[1,2,3,4,5,6,7,8,9]
g,l=find_max_min(numbers)
print(f"Max: {g}\n Min: {l}")