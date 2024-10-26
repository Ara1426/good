def cube(x):
    return x*x*x
def malik(x):
    if x%3 ==0:
        return cube(x)
    else:
        return False
print(malik(27))
print(malik(2))
