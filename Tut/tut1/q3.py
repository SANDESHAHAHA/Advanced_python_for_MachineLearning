#3. Write a program to count the number of vowels in a given string.

sent=str(input("Enter the string: "))

def count_vowels(sent):
    count_vowels=0
    vowel_list=['a','e','i','o','u']
    for word in sent.lower().split():
        for letters in word:
            if letters in vowel_list:
                count_vowels+=1
    return count_vowels

print(f"The count of vowels is : {count_vowels(sent)}") 