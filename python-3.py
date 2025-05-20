def series(a):
    r=[]
    for i in range(a):
        num=2*i+1
        r.append(num)
    print("Output:", ", ".join(map(str, r)))
a=int(input("Enter a number:"))
if a%2==0:
    series(a-1)
else:
    series(a)
