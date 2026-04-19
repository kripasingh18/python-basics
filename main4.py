s=input("enter a multidigit number: ")
d={}
print("the frequency of each digit in the given number is:  ")
for ch in s:
    d[ch]=d.get(ch,0)+1
print (d)
