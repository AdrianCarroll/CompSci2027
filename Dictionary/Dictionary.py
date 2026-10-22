def sort_dict(a):
    return a[1]
book=open("book.txt", "r")
start=book.read()
thing=start.split()
diction={}
for i in thing:
    if i in diction:
        diction[i]=(diction[i]+1)
    else:
        diction[i]=1
sortdiction = sorted(diction.items(),key=sort_dict, reverse=True)
print(sortdiction[0:10])