
from bintreeFile import Bintree
svenska = Bintree()
engelska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            pass 
        else:
            svenska.put(ordet)             # in i sökträdet
with open("engelska.txt", "r", encoding = "utf-8") as engelskafil:
    for rad in engelskafil:
        orden = rad.strip().split()                # Ett trebokstavsord per rad
        for ordet in orden:
            if ordet in engelska:
                pass 
            else:
                engelska.put(ordet)             # in i sökträdet
                if ordet in svenska:   
                    print(ordet, end = " ") 
   
print("\n")