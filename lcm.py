def findlcm(a,b):
    greater = max(a,b)
    while True:
        if greater %a == 0 and greater % b == 0:
            return greater
        greater = greater+1

print(findlcm(4,5))