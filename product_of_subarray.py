def multipli(arr):
    current = 1
    maximum = 1
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            current = arr[i] * arr[j]
            maximum = max(maximum,current)
    return maximum

array = [2,3,4,6,7]
print(multipli(array))