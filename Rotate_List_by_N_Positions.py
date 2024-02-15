n=int(input())
a=list(map(int,input().split()))
r=int(input())
for i in range(r):
    c=a[n-1]
    a.pop(n-1)
    a.insert(0,c)
print(*a)