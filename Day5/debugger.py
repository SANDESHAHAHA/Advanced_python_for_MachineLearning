import pdb
# x=[1,2,3,4,5]
# pdb.set_trace()
# for i in range(100):
#     y=x.pop()
#     print(y)

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
pdb.set_trace()
fact(5)