import sys
file_name= sys.argv[1]
m=[]
f=open(file_name,'r')
for line1 in f:
    m.append(list(map(int,line1.strip().split(" "))))
def checkx(m):
    r1 =None
    s1=None
    for r in range(len(m)):
        for s in range(len(m)-4):
            if m[r][s]==1 and m[r][s+1]==1 and m[r][s+2]==1 and m[r][s+3]==1 and m[r][s+4]==0:
                s1=s+4
                r1=r
            if m[r][s] == 1 and m[r][s + 1] == 1 and m[r][s + 2] == 1 and m[r][s + 3] == 0 and m[r][s + 4] == 1:
                s1 = s + 3
                r1 = r
            if m[r][s] == 1 and m[r][s + 1] == 1 and m[r][s + 2] == 0 and m[r][s + 3] == 1 and m[r][s + 4] == 1:
                s1 = s + 2
                r1 = r
            if m[r][s] == 1 and m[r][s + 1] == 0 and m[r][s + 2] == 1 and m[r][s + 3] == 1 and m[r][s + 4] == 1:
                s1 = s + 1
                r1 = r
            if m[r][s] == 0 and m[r][s + 1] == 1 and m[r][s + 2] == 1 and m[r][s + 3] == 1 and m[r][s + 4] == 1:
                s1 = s
                r1 = r
    return ( r1,s1)
def checky(m):
    r1 =None
    s1=None
    for r in range(len(m)-4):
        for s in range(len(m)):
            if m[r][s]==1 and m[r+1][s]==1 and m[r+2][s]==1 and m[r+3][s]==1 and m[r+4][s]==0:
                s1=s
                r1=r+4
            if m[r][s] == 1 and m[r+1][s] == 1 and m[r+2][s] == 1 and m[r+3][s] == 0 and m[r+4][s] == 1:
                s1 = s
                r1 = r+3
            if m[r][s] == 1 and m[r+1][s] == 1 and m[r+2][s] == 0 and m[r+3][s ] == 1 and m[r+4][s] == 1:
                s1 = s
                r1 = r+2
            if m[r][s] == 1 and m[r+1][s] == 0 and m[r+2][s] == 1 and m[r+3][s] == 1 and m[r+4][s] == 1:
                s1 = s
                r1 = r+1
            if m[r][s] == 0 and m[r+1][s ] == 1 and m[r+2][s] == 1 and m[r+3][s ] == 1 and m[r+4][s] == 1:
                s1 = s
                r1 = r
    return ( r1,s1)
def checkxy(m):
    r1 =None
    s1=None
    for r in range(len(m)-4):
        for s in range(len(m)-4):
            if m[r][s]==1 and m[r+1][s+1]==1 and m[r+2][s+2]==1 and m[r+3][s+3]==1 and m[r+4][s+4]==0:
                s1=s+4
                r1=r+4
            if m[r][s] == 1 and m[r+1][s+1] == 1 and m[r+2][s+2] == 1 and m[r+3][s+3] == 0 and m[r+4][s+4] == 1:
                s1 = s+3
                r1 = r+3
            if m[r][s] == 1 and m[r+1][s+1] == 1 and m[r+2][s+2] == 0 and m[r+3][s+3 ] == 1 and m[r+4][s+4] == 1:
                s1 = s+2
                r1 = r+2
            if m[r][s] == 1 and m[r+1][s+1] == 0 and m[r+2][s+2] == 1 and m[r+3][s+3] == 1 and m[r+4][s+4] == 1:
                s1 = s+1
                r1 = r+1
            if m[r][s] == 0 and m[r+1][s+1 ] == 1 and m[r+2][s+2] == 1 and m[r+3][s+3 ] == 1 and m[r+4][s+4] == 1:
                s1 = s
                r1 = r
    return ( r1,s1)
def checkyx(m):
    r1 =None
    s1=None
    for r in range(0,len(m)-4):
        for s in range(4,len(m)):
            if m[r][s]==1 and m[r+1][s-1]==1 and m[r+2][s-2]==1 and m[r+3][s-3]==1 and m[r+4][s-4]==0:
                s1=s-4
                r1=r+4
            if m[r][s] == 1 and m[r+1][s-1] == 1 and m[r+2][s-2] == 1 and m[r+3][s-3] == 0 and m[r+4][s-4] == 1:
                s1 = s-3
                r1 = r+3
            if m[r][s] == 1 and m[r+1][s-1] == 1 and m[r+2][s-2] == 0 and m[r+3][s-3 ] == 1 and m[r+4][s-4] == 1:
                s1 = s-2
                r1 = r+2
            if m[r][s] == 1 and m[r+1][s-1] == 0 and m[r+2][s-2] == 1 and m[r+3][s-3] == 1 and m[r+4][s-4] == 1:
                s1 = s-1
                r1 = r+1
            if m[r][s] == 0 and m[r+1][s-1 ] == 1 and m[r+2][s-2] == 1 and m[r+3][s-3 ] == 1 and m[r+4][s-4] == 1:
                s1 = s
                r1 = r
    return ( r1,s1)
if checky(m)[0] and checky(m)[1]  != None:
    print(checky(m)[0], checky(m)[1])
if checkx(m)[0] and checkx(m)[1] !=None:
    print(checkx(m)[0], checkx(m)[1])
if checkyx(m)[0] and checkyx(m)[1]!=None:
    print(checkyx(m)[0], checkyx(m)[1])
if checkxy(m)[0] and checkxy(m)[1] !=None:
    print(checkxy(m)[0], checkxy(m)[1])
