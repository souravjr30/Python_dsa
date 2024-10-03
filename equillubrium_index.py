def index(arr):
    total = sum(arr)
    left_sum = 0
    for i in range(len(arr)):
        if left_sum == total - left_sum - arr[i]:
            return i
        left_sum = left_sum + arr[i]

    return -1

array = [1,3,5,2,2]
print(index(array))
