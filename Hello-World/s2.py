word="good morning"
for ch in word:
    count=0
    for i in word:
        if ch==i:
            count=count+1
    print(ch,"=",count)        