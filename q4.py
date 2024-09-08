p=input().strip()
n=int(input())
sp=sorted(p,reverse=True)
if list(set(sp[1::]))==["0"]:
    print(*sp[0:n-1])
else:
    print(*sp[n::])