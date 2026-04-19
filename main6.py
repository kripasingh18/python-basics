my_dict=[]
n=int(input("enter the number of key value pairs:"))
for i in range (n):
    num=int(input("enter the number:"))
    my_dict.append(num)
print("my list:",my_dict)
file=open("numbers.txt","w")
for num in my_dict:
    if num%2==0:
        file.write(str(num)+"\n")
file.close()