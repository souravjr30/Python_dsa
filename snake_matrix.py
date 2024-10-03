def snake_matrix(n):
    matrix = [[(i*n)+j+1 for j in range(n)] for i in range(n)]
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        if i%2==0:
            for j in range(col):
                print(matrix[i][j],end=" ")
        else:
            for j in range(col-1,-1,-1):
                print(matrix[i][j],end=" ")
        print()
snake_matrix(3)