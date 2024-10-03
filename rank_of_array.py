def rankof(arr):
    unique = sorted(set(arr))
    rank = []
    for i in arr:
        rankis = unique.index(i)
        rank.append(rankis+1)
    return rank

array = [9,7,8,8,5,2,9]
print(rankof(array))