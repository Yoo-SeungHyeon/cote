n = input()
a = list(map(int,input().split()))
x = int(input())
count = 0
for i in a:
    t = x - i
    if t in a:
        count = count+1
print(count//2)