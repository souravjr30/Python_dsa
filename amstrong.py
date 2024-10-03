n = int(input("Enter the number: "))
order = len(str(n))
sum=0
temp = n
while temp>0:
    digit = temp%10
    sum += digit ** order
    temp = temp//10

if n == sum:
    print("Amstrong")
else:
    print("not")
