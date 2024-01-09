class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

N,K = map(int,input().split())

node_1 = Node(1)
for i in range(N-1):
    globals()[f"node_{i+2}"] = Node(i+2)
    globals()[f"node_{i+1}"].next = globals()[f"node_{i+2}"]

globals()[f"node_{N}"].next = node_1

header = globals()[f"node_{N}"]
result = []

for l in range(N):    
    for j in range(K-1):
        target = header.next
        header = target
    result.append(str(target.next.data))
    target.next = target.next.next
print('<',", ".join(result),">", sep='')