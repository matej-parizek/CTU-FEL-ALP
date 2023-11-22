import sys
file_name= sys.argv[1]
class Stone():
    def __init__(self,collor,souradnice):
        self.collor=collor
        r=[]
        s=[]
        for i in range(0,len(souradnice)-1,2):
            s.append(souradnice[i+1])
            r.append(souradnice[i])
        maxSloupec=max(s)
        maxRadek=max(r)
        minSloupec=min(s)
        minRadek=min(r)
        osax= -1*minSloupec
        osay=-1*minRadek
        self.vyska= osay + maxRadek +1
        self.sirka= osax + maxSloupec +1
        self.policka=[]
        for i in range(0,len(souradnice)-1,2):
            radek=souradnice[i] + osay
            sloupec=souradnice[i+1]+osax
            self.policka.append([radek,sloupec])

    def mimoradek(self, osay):
        return self.vyska + osay > M

    def mimosloupec(self, osax):
        return osax + self.sirka > N
def len_s(s):
    return len(s.policka)
def readStones(filename):
    stones = []  # vystup funkce - seznam nactenych kamenu
    f = open(filename, "r")
    numRows = int(f.readline().strip())  # precti 1. radek ze souboru
    numCols = int(f.readline().strip())  # precti 2. radek ze souboru
    numStoneFields=0
    for line in f:
        numbers = list(map(int, line.strip().split()))  # precti vsechna cisla na dalsich radcich
        s = Stone(numbers[0],numbers[1:])
        numStoneFields += len(s.policka)
        stones.append(s)
    f.close()
    stones.sort(reverse=True, key=len_s);
    return numRows, numCols, numStoneFields, stones
def Pole():
    pole=[]
    pol=[]
    for i in range(M):
        for j in range(N):
            pol.append(0)
        pole.append(list(map(int, pol)))
        pol =[]
    return pole
def spojeni(n):
    global Reseni
    if n == len(kameny):
        print(pole)
        Reseni = False
        return
    for posunR in range(M-kameny[n].vyska + 1):
        if kameny[n].mimoradek(posunR):
            break
        for posunS in range(N-kameny[n].sirka + 1):
            if kameny[n].mimosloupec(posunS):
                break
            volno=True
            for souradnice in kameny[n].policka:
                if pole[souradnice[0]+posunR][souradnice[1]+posunS]!=0:
                    volno= False
                    break
            if volno==False:
                continue
            for souradnice in kameny[n].policka:
                pole[souradnice[0]+posunR][souradnice[1]+posunS]= kameny[n].collor
            spojeni(n+1)
            if Reseni ==False:
                return
            for souradnice in kameny[n].policka:
                pole[souradnice[0] + posunR][souradnice[1] + posunS] = 0
    return
M, N, X, kameny = readStones(file_name);
pole=Pole()
Reseni=True
if X == M * N:  # celkovy pocet policek vsech kamenu odpovida velikosti hraci plochy
    spojeni(0)
if Reseni:
    print("NOSOLUTION")