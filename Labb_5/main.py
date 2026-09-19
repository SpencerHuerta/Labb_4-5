
from bintreeFile import Bintree
from linkedQFile import LinkedQ

q = LinkedQ()
alfabet = list("abcdefghijklmnopqrstuvwxyzåäö")
svenska = Bintree()
gamla = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            pass 
        else:
            svenska.put(ordet)             # in i sökträdet


def makechildren(ord,q,slutord):
    gamla.put(ord)
    letters = list(ord)
    for bokstav in alfabet:
        for i in range(len(letters)):
            nyttord = list(letters)
            nyttord[i] = bokstav
            nyttord = nyttord[0] + nyttord[1] + nyttord[2]
            if nyttord in svenska and nyttord not in gamla:
                gamla.put(nyttord)
                q.enqueue(nyttord)
                if slutord == nyttord:
                    print("Det finns en väg till", slutord)
                    return True
    return False            

def main():
    [startord, slutord] = input("Startord Slutord: ").split()
    q.enqueue(startord)
    stop = False
    while not q.isEmpty() and not stop:
        ord = q.dequeue()
        stop = makechildren(ord,q,slutord)
    if stop == 0:
        print('Det finns ingen väg till',slutord)
if __name__ == "__main__":
    main()