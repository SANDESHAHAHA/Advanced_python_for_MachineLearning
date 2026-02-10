#command line argument 

import random 
import sys 

print("hello world")
print(sys.argv)

n = int(sys.argv[1])
f=1
for i in range(1,n+1):
    f=f*i
print(f)

