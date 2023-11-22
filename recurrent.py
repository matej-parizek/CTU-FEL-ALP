n = int(input())
x = float(input())
e =10**-8
R = [-1, x, -x ** 2]
def recur(n,x,y,R):
    V=[]
    if y>=n:
        Rn= (((1 / n) * R[2]) + ((-1) ** n) * (n / (n + 1)) * R[1] + ((n - 1) / x) * R[0])
        V= [R[1],R[2],Rn]
        n+=1
        return recur(n,x,y,V)
    return R[2]
vysledek = recur(3,x,n,R)
print(vysledek)