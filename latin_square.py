def latin_square(n):
    row = [chr(65+i) for i in range(n)]  #row = [i for i in range(1,n+1] for printing integers
    new_num = []
    for i in range(n):
        shifted_row = row[i:]+row[:i]
        new_num.append(shifted_row)
    return new_num

result = latin_square(4)
for r in result:
    print(r)

