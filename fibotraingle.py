row = int(input("Enter the number of rows:"))
n = (row*(row+1))//2

series = [1, 1]
for i in range(2, n):
    num = series[-1]+series[-2]
    series.append(num)

num = 0
for i in range(row):
    for j in range(i+1):
        print(series[num], "", end=" ")
        num = num+1
    print()




