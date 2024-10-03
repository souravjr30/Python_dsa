#write a program to find the prime numbers in the range [a,b] inclusive of a and b

def checkprime(n):
    if n <= 1:
        return False
    else:
        for i in range(2,int(n ** 0.5) + 1):
            if n % i == 0:
                return False

        return True



def print_prime(a, b):
    if a>=0 and b>=0 and a<=b:
        for num in range(a,b+1):
            if checkprime(num):
                print(num, end=" ")
    else:
        print("provide valid input")


a = int(input())
b = int(input())
print_prime(a, b)