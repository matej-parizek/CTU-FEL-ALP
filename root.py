a5 = int(input())
a4 = int(input())
a3 = int(input())
a2 = int(input())
a1 = int(input())
a0 = int(input())
# presnost
e = 10**-9

# podeminky
if (-1*a0) > 0:
    x1 = 0
    x2 = (-1*a0)

elif (-1*a0) < 0:
    x1 = (-1*a0)
    x2 = 0

else:
    x1 = 1
    x2 = -1
x = 0
while abs(x1-x2) > e:
    x = (x1+x2)/2
    k = (a5 * x ** 5) + (a4 * x ** 4) + (a3 * x ** 3)+(a2 * x ** 2)+(a1 * x) + a0
    if k < 0:
        x1 = x
    else:
        x2 = x
print(x)