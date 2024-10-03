str = input()
for i in range(0,len(str),2):
    g = str[i]+str[i+1]
    h = int(g)
    print(chr(h))

#convert ascci to character