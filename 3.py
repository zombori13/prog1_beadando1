

lista = ["Hello", "World", "in", "a", "frame"]

def keretezo (lista):
    mszh=0
    for szo in lista:
        if mszh<len(szo):
            mszh=len(szo)

    print('*'*(4+mszh))
    for szo in lista:
        if len(szo)<mszh:
            print('*', szo, ' ' * (mszh - len(szo)-1), '*')
        else:
            print('*', szo,'*')
    print('*' * (4 + mszh))


keretezo(lista)