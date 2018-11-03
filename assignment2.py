def sumofsquares(n):
    for i in range(1,n+1):
        if isSquare(i) and isSquare(n-i):
            return True
    return False

    
def isSquare(n):
    if n==0:
        return False
    for i in range(2,n+1):
        if n%i==0 and isPrime(i) and OddPowerOf(i,n):
            return False
    return True

def isPrime(n):
    f=0
    for i in range(1,n+1):
        if n%i==0:
            f=f+1
    return (f==2)


def OddPowerOf(i,n):
    c=0
    while n%i==0:
        c=c+1
        n=n/i
    return (c%2==1)

def show(n):
    for i in range(1,n+1):
        if sumofsquares(i):
            print(i)

def wellbracketed(s):
    nest=0
    for i in range(0,len(s)):
        if s[i]=='(':
            nest=nest+1
        if s[i]==')':
            nest=nest-1
    return (nest==0)


def rotatelist(l,k):
    rotate=l[:]
    for i in range(1,k+1):
        r=[rotate[len(l)-1]]
        rotate=r+rotate[:len(l)-1]
        print(r)
    return rotate

----**----
