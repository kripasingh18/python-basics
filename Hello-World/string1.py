word="school"
letter='k'
index=0
flag=False
while index<len(word):
    if word[index]==letter:
        print("found")
        flag=True
        break
    index=index+1
if not flag:
    print("not found")    
