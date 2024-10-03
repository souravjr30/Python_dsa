def add_in_end(arr,ele):
    arr.append(ele)
def add_in_begining(arr,ele):
    arr.insert(0,ele)
def add_in_specific(arr,ele,k):
    arr.insert(k,ele)

array = [5,4,6,3,5,6]
element = 5
k = 2

add_in_end(array,element)
print(array)