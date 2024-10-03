def kth_smallest(matrix, k):
    flat_list = []
    for row in matrix:
        flat_list.extend(row)

    flat_list.sort()
    return flat_list[k - 1]

'''Given an n x n matrix where each of the rows and columns is sorted in ascending order, find the kth smallest element in the matrix. Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8 Output: 13'''