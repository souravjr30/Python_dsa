def rotate(arr,k):
    n = len(arr)
    k = k % n
    rotated_array = arr[-1:] + arr[:-1]  #want to rotate in other direction change it to arr[1:] + arr[:1]
    return rotated_array

array = [3,5,6,7,8]
k = 3
print(rotate(array,k))