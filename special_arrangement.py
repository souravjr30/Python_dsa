def arrangement(arr):
    arr.sort()
    n = len(arr)
    i,j = 0,n-1
    result = []
    while i<=j:
        if i<=j:
            result.append(j)
            j=j-1
        if i<=j:
            result.append(i)
            i=i+1
    return result

new_arr = [1,4,6,3,7,9,8]
print(arrangement(new_arr))


'''given an array of integers,rearrange the array that first element is firet maximum and second element is first minimum'''