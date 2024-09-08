n=int(input())
s=input().strip()
d=list(map(str,input().split()))
res=""
for i in d:
    if i in s and i not in res:
        res+=i
if res==s:
    print(1)
else:
    print(0)