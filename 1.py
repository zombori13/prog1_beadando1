
db=1
szam=3
prim = int(input('Adja meg hanyadik primszam kell: '))
while ( db<prim ):
    for i in range (szam//2,0,-2):
        if i%2==0:
            i-=1
        if szam%i == 0:
            if i==1:
                db += 1
                break
            else:
                break
    szam += 2
print("A {}. primszám: {}".format(db, szam-2))
