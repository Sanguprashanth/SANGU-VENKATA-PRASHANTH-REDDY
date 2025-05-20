def count(l):
    res={}
    for i in range(1,10):
        c=0
        for item in l:
            if item%i==0:
                c+=1
        res[i]=c
    return res
l=[1,10,16,6,9,15]
output=count(l)
print(output)
