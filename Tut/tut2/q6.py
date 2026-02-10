# 6. Write a generator expression to create a list of cubes of numbers from 1 to 20
def cubeList():
    cubes=[]
    for i in range(1,21):
        result = yield i*i*i
        cubes.append(result)
    return cubes

print(*cubeList())