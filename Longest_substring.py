str = input()
list = []
maxlist = []
max = 0
for i in str:
    if i not in list:
        list.append(i)
    lens = len(list)
    if lens>max:
        max=lens
        maxlist = list

print(max)

'''Given a string, find the length of the longest substring without repeating 
characters.
Input:
s = "abcabcbb"
Output:3  '''