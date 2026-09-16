
from bintreeFile import Bintree
from linkedQFile import LinkedQ


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


[startord, slutord] = input("Startord Slutord: ").split()


def makechildren(ord):
    gamla.put(ord)
    letters = list(ord)
    for bokstav in alfabet:
        for i in range(len(letters)):
            nyttord = list(letters)
            nyttord[i] = bokstav
            nyttord = nyttord[0] + nyttord[1] + nyttord[2]
            if nyttord in svenska and nyttord not in gamla:
                gamla.put(nyttord)
                print(nyttord, end=' ')
    print('\n')


        # nyttord1 = bokstav + letters[1] + letters[2]
        # nyttord2 = letters[0] + bokstav + letters[2]
        # nyttord3 = letters[0] + letters[1] + bokstav

        # if nyttord1 in svenska and nyttord1 not in gamla:
        #     gamla.put(nyttord1)

        # if nyttord2 in svenska and nyttord2 not in gamla:
        #     gamla.put(nyttord2)

        # if nyttord3 in svenska and nyttord3 not in gamla:
        #     gamla.put(nyttord3)
        


makechildren(startord)
