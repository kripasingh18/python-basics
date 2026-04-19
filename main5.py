my_dict={}
n=int(input("enter the number of key value pairs:"))
for i in range (n):
    key=input("enter the key:")
    value=input("enter the value:")
    my_dict[key]=value
sorted_dict=dict(sorted(my_dict.items()) )
print("original dictionary:",my_dict)
print("sorted dictionary:",sorted_dict)   