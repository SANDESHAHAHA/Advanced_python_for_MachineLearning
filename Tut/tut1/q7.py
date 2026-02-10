#7. Write a program to check if a string is a palindrome.

def palindrome(string):
    n=len(string)
    for i in range(0,n):
        if string[i] == string[n-i-1]:
            return True
        else:
            return False
sent=str(input("Enter a string: "))
print(palindrome(sent))