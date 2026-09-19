
from bintreeFile import Bintree
from linkedQFile import LinkedQ


class ParentNode:
    def __init__(self,word,parent = None):
        self.word = word
        self.parent = parent





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

def writechain(ordnod):
    if ordnod.parent == None:
        return ordnod.word
    return writechain(ordnod.parent) + ' ' + ordnod.word

def makechildren(ordnod,q,slutord):
    ord = ordnod.word
    gamla.put(ord)
    letters = list(ord)
    for bokstav in alfabet:
        for i in range(len(letters)):
            nyttord = list(letters)
            nyttord[i] = bokstav
            nyttord = nyttord[0] + nyttord[1] + nyttord[2]
            if nyttord in svenska and nyttord not in gamla:
                gamla.put(nyttord)
                q.enqueue(ParentNode(nyttord,ordnod))
                
                
                if slutord == nyttord:
                    print("Det finns en väg till", slutord)
                    print(writechain(ParentNode(nyttord,ordnod)))
                    return True
    return False            

def main():
    [startord, slutord] = input("Startord Slutord: ").split()
    q.enqueue(ParentNode(startord))
    stop = False
    while not q.isEmpty() and not stop:
        ord = q.dequeue()
        stop = makechildren(ord,q,slutord)
    if stop == 0:
        print('Det finns ingen väg till',slutord)
    
if __name__ == "__main__":
    main()