num=int(input("enter a number:"))
def factorial(n):
    if n<0:
        print("factorial not exist for negative numbers")
    elif n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print("factorial of the given num is: ",factorial(num))        