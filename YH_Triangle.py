#YH_Triangle


def triangle():
   
    L = [1]
    while 1:
        yield L
        r = []
        for i in range(len(L)-1):            
            r.append(L[i] + L[i+1])  
        L = [1] + r +[1]
        #L = [1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1]

n = 0
results = []
for t in triangle():
    results.append(t)
    n = n + 1
    if n == 10:
        break  
    
for i in results:
    print(i)

