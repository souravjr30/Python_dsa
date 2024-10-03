def hcf(x,y):
    while(y):
        x, y = y, x%y
    return x
num = hcf(500,50)
print(num)