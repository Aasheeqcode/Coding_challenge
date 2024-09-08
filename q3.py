n=int(input())
m=int(input())
for i in range(n,m+1):
    s=str(i)
    ss=sorted(s)
    p=1
    for j in range(len(ss)-1):
        res=int(ss[j])-int(ss[j+1])
        if res!=-1 and res!=0:
            p=0
            break
    if p==1:
        print(i)
 
