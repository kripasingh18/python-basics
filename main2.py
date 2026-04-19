num=int(input("enter the no of terms: "))
def fibb(n):
    if n<=1:
        return n
    else:
        return(fibb(n-1)+fibb(n-2))
if num<=0:
    print("Please enter a positive integer")
else:
    for i in range(0,num,1):
        print(fibb(i))    

