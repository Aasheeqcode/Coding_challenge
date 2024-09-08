l=list(map(int,input().split()))
m=int(input())
maxi,s,cs=0,0,0
for i in range(len(l)):  
    cs+= l[i]  
    while cs>m:  
        cs-=l[s]  
        s+=1  
    maxi = max(maxi, i-s+ 1)  
print(maxi)