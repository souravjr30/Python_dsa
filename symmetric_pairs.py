def symetric_pairs(arr):
    symmetric = []
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][0] == arr[j][1] and arr[i][1] == arr[j][0] and i!=j:
                symmetric.append((arr[i],arr[j]))
    return symmetric

array = [(2,1),(2,2),(1,1),(1,2)]
print(symetric_pairs(array))