def dupli(arr):
    if not arr:
        return []
    unique_arr = [arr[0]]
    for i in range(1,len(arr)-1):
        if arr[i] != unique_arr[-1]:
            unique_arr.append(arr[i])
    return unique_arr

array = [5,4,3,5,4,4,4,5,3,3]
print(dupli(array))