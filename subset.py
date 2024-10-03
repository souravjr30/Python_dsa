'''def subset(arr1,arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return set2.issubset(set1)

array1 = [3,4,5,6,7,10,1,2,3]
array2 = [3,4,5,6]

print(subset(array1,array2))
'''
def subset(arr1,arr2):
    for i in range(len(arr1)):
        if i in arr2:
            return True
    return False

array1 = [3,4,5,6,7,10,1,2,3]
array2 = [3,4,5,6]

print(subset(array1,array2))