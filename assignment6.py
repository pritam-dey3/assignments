l = [100,97,93,38,67,54,93,17,25,42]
def insertHeap(l,n):
    l.append(n)
    loop = True
    i = len(l)-1
    while(loop):
        j = (i-1)//2
        loop = False
        if (l[j] < l [i]):
            (l[i],l[j]) = (l[j],l[i])
            i = j
            loop = True
        if i == 0:
            loop = False

def delHeap(l):
    i = len(l)-1
    (l[0],l[i]) = (l[i],l[0])
    l.pop()
    i = 0
    loop = True
    while(loop):
        loop = False
        try:
            a = l[2*i + 1]
        except IndexError:
            break
        try:
            if (a > l[2*i + 2]):
                j = 2*i + 1
            else:
                j = 2*i + 2
        except IndexError:
            j = 2*i + 1
        if (l[i] < l[j]):
            (l[i],l[j]) = (l[j],l[i])
            i = j
            loop = True
        
        

        
delHeap(l)
delHeap(l)
print(l)


    
