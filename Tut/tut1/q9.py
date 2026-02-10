# 9. Write a Python function that reads a text file and counts the number of lines.

with open("q9textfile.txt","r") as f:
    lines = f.readlines()
    print(len(lines))
    