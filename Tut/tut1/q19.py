#19. Write a Python program to check if two strings are anagrams of each other.

from collections import Counter
import re

def check_anagrams(str1,str2):
    
    cleaned_str1=re.sub('[^a-zA-Z0-9]','',str1)
    cleaned_str2=re.sub('[^a-zA-Z0-9]','',str2)
    
    if len(cleaned_str1)!=len(cleaned_str2):
        return False
    
    return Counter(cleaned_str1)==Counter(cleaned_str2)


sent1=str(input("Enter first word: "))
sent2=str(input("Enter second word: "))

print(f"Are anagrams: {check_anagrams(sent1,sent2)}")