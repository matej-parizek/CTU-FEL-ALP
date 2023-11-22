import sys
tabulka= sys.argv[1]
pole=[]
f=open(tabulka,'r')
for line1 in f:
    pole.append(list(map(str,line1.strip())))
slova= sys.argv[2]
word=[]
f=open(slova,'r')
for line1 in f:
    word.append(list(map(str,line1.strip())))
tabulka2=pole[:][:]

def findx(word,pole):
    tabulkax=[]
    tabulkay=[]
    len_word=[]
    for i in range(len(word)):
        for j in range(len(pole)): #řádky
            for k in range(len(pole[j])-len(word[i])+1): #sloupce
                if pole[j][k:k+len(word[i])] == word[i]:
                    tabulkax.append(k)
                    tabulkay.append(j)
                    len_word.append(len(word[i]))
    return tabulkax, tabulkay,len_word  # sloupec, řádek
def findy(word,pole):
    slovo=[]
    tabulkax = []
    tabulkay = []
    len_word = []
    for i in range(len(word)):
        for j in range(len(pole[0])):
            if len(pole)-len(word[i])>=0:
                for k in range(len(pole)-len(word[i])+1):
                    for l in range(len(word[i])):
                        slovo.append(pole[k+l][j])
                    if slovo == word[i]:
                        tabulkax.append(k)
                        tabulkay.append(j)
                        len_word.append(len(word[i]))
                    slovo =[]
    return tabulkax, tabulkay, len_word, #sloupec, řádek
def findxy(word,pole):
    slovo=[]
    tabulkax = []
    tabulkay = []
    len_word = []
    for i in range(len(word)):
        for j in range(len(pole[0])-len(word[i])+1):
            if len(pole)-len(word[i])>=0:
                for k in range(len(pole)-len(word[i])+1):
                    for l in range(len(word[i])):
                        slovo.append(pole[k+l][j+l])
                    if slovo == word[i]:
                        tabulkax.append(k)
                        tabulkay.append(j)
                        len_word.append(len(word[i]))
                    slovo =[]
    return tabulkax,tabulkay,len_word
def findyx(word,pole):
    slovo = []
    tabulkax = []
    tabulkay = []
    len_word = []
    for i in range(len(word)):
        for j in range(len(pole[0])-1,len(word[i])-1,-1):
            if len(pole)-len(word[i])>=0:
                for k in range(len(pole)-1,len(word[i])-1,-1):
                    for l in range(len(word[i])):
                        slovo.append(pole[k-l][j-l])
                    if slovo == word[i]:
                        tabulkax.append(k)
                        tabulkay.append(j)
                        len_word.append(-len(word[i]))
                    slovo =[]
    return tabulkax,tabulkay,len_word
x_r = findx(word,pole)[1]
x_s = findx(word,pole)[0]
x_len = findx(word,pole)[2]

y_s = findy(word,pole)[1]
y_r = findy(word,pole)[0]
y_len = findy(word,pole)[2]

xy_s = findxy(word,pole)[1]
xy_r = findxy(word,pole)[0]
xy_len = findxy(word,pole)[2]

yx_r = findyx(word,pole)[1]
yx_s = findyx(word,pole)[0]
yx_len = findyx(word,pole)[2]

def pole1(xr,xs,xl,pole):
    for i in range(len(xr)):
        for j in range(xl[i]):
            pole[xr[i]][xs[i]+j]="1"
    return pole
def pole2(yr,ys,yl,pole1):
    for i in range(len(yr)):
        for j in range(yl[i]):
            pole1[yr[i]+j][ys[i]]="1"
    return pole1
def pole3 (xyr,xys,xyl,pole2):
    for i in range(len(xyr)):
        for j in range(xyl[i]):
            pole2[xyr[i]+j][xys[i]+j]="1"
    return pole2
def pole4 (xyr,xys,xyl,pole2):
    for i in range(len(xyr)):
        for j in range(xyl[i]):
            pole2[xyr[i]-j][xys[i]-j]="1"
    return pole2
def tisk(pole):
    for i in range(len(pole)):
        for j in range(len(pole[i])):
            if pole[i][j]!="1":
                print(pole[i][j],end="")
pole_1= pole1(x_r,x_s,x_len,pole)
pole_2= pole2(y_r,y_s,y_len,pole_1)
pole_3= pole3(xy_r,xy_s,xy_len,pole_2)
pole_4=pole4(yx_r,yx_s,yx_len,pole)
tisk(pole_4)