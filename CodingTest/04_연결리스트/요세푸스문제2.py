n,k=map(int,input().split())
a= [i+1 for i in range(n)]
r=[]
for i in range(n-k+1):
    r.append(a[k-1])
    a=a[k:]+a[:k-1]

for j in range(k-2):
    out=k%len(a)
    r.append(a[out-1])
    a=a[out:]+a[:out-1]
print('<', end='')
for l in range(n-1):
    print(f'{r[l]},',end=' ')
print(f'{a[0]}>')