#16. Write a program to count the frequency of each word in a given string.

def count_freq(sent):
    aDict={}
    for word in sent.split():
        if word not in aDict:
            aDict[word]=1
        else:
            aDict[word]+=1
    return aDict

sentence=str(input("Enter a string to calculate frequency of words: "))
print(f"The counts of words are: {count_freq(sentence)}")