def frequency(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq
def sort_by_frequency(arr):
    freq = frequency(arr)
    sorted_array = sorted(array, key=lambda x: (freq[x], x))  #for sorting in descending order make it (-freq[x],-x)
    return sorted_array

array = [3,4,3,3,3,3,2,5]
print(sort_by_frequency(array))


