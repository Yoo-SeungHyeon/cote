import sys
sent = list(sys.stdin.readline().strip())
point = len(sent)

n = int(input())

for i in range(n):
    comm = list(input())
    
    if comm[0] == 'L':
        if point > 0:
            point = point -1
            
    elif comm[0] == 'D':
        if point < len(sent):
            point = point + 1
            
    elif comm[0] == 'B':
        sent = sent[point:]
        point = 0
        
    elif comm[0] == 'P':
        if point == 0:
            sent = [comm[2]] + sent
            point = point + 1
        elif point == len(sent):
            sent = sent + [comm[2]]
            point = point + 1
        else:
            sent = sent[:point] + [comm[2]] + sent[point:]
            pint = point + 1
print(''.join(sent))