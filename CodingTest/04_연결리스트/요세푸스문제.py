import sys
N, K = map(int,sys.stdin.readline().split())

a = [i for i in range(1,N+1)]
out = K-1
result = []

while(1):
    if len(a) >= K:
        result.append(str(a[out]))
        a = a[K:] + a[:out]
    elif len(a) == 1:
        result.append(str(a[0]))
        del a[0]
        break
    else:
        out = K%len(a)
        result.append(str(a[out-1]))
        a = a[out:] + a[:out-1] 
print('<', ', '.join(result),'>', sep = '')