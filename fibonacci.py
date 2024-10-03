n = int(input("Enter the number:"))
a, b =0, 1
sum=0
for i in range(n):
    print(sum,end=" ")
    a=b
    b=sum
    sum=a+b


