a = int(input())
b = int (input())
def gcd (x,y):
    while (y != 0):
        x,y=y,x % y
    return x
def gce (a,b):
    if a < b:
        a,b =b,a
    zb=a%b
    while (zb!=0):
        a=b
        b=zb
        zb=a%b
    return b
def prvocislo(n):
    n=abs(n)
    if (n==1) or (n==0):
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

if a<2 or a==b or b<2:
    print("ERROR")
    exit()
for m in range(min(a,b),max(a,b)+1):
    for n in range(min(a,b),max(a,b)+1):
        if n !=min(a,b):
            print("|",end="")
        if gcd(n,m)>=2:
                print("x", end="")
        elif prvocislo(n) or prvocislo(m):
            print( "p",end="")

        else:
            print(" ",end="")
    print()
    if (m<max(a,b)):
        for i in range(min(a,b),max(a,b)+1):
            if i < max(a,b):
                print("--",end="")
            else:
                print("-",end="")
    print()

