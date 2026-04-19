import numpy as np
list=[]
n=int(input("enter the number of elements:"))
print("enter the elements:")
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print("original list:",list)
print("mean:",np.average(list))
print("variance:",np.var(list))
print("standard deviation:",np.std(list))
    