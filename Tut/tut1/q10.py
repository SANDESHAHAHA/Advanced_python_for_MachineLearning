# 10. Create a program to sort a list of tuples based on the second element
aList=[("prashant",20,False),
       ("anjil",18,False),
       ("ajay",24,True)]
bList=sorted(aList,key=lambda x: x[1])
print(bList)
