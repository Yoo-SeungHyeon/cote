n = int(input())

for i in range(n):
    m = list(input())
    L = len(m)
    sent = []
    point = 0
    for j in m:
        if j == '<':
            if point == 0: point = 0
            else : point -= 1
        elif j == '>':
            if point == len(sent): point = len(sent)
            else : point += 1
        elif j == '-':
            if point == 0: 
                sent = sent

            elif point == len(sent):
                sent = sent[:-1]
                point -= 1
            else:
                sent = sent[:point-1] + sent[point:]                
        else:
            if point == 0: 
                sent = [j] + sent
                point += 1                
            elif point == len(sent): 
                sent = sent + [j]
                point = point + 1                
            else: 
                sent = sent[:point] + [j] + sent[point:]
                point += 1                
    
    print(''.join(sent))