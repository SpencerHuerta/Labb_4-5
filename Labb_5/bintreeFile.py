

class Bintree:
    def __init__(self):
        self.root = None
        
    def put(self, newvalue):
        if not self.__contains__(newvalue):
            self.root = putta(self.root,newvalue)
        else:
            pass
            #print(newvalue, " finns redan i trädet!")
    def __contains__(self, value):
        return finns(self.root,value)

    def write(self):
        skriv(self.root)
        print("\n")


class Node:
    def __init__(self, data,head=None,left=None,right=None):
        self.value = data
        self.head = head
        self.left = left
        self.right = right
        

def putta(p, newvalue):
    if p == None:
        p = Node(newvalue)
        p.head = p
        return p
    else:
        previous = None
        current = p
        
        while current != None:
            if newvalue < current.value:
                previous = current
                current = current.left 
               
            elif newvalue > current.value:
                previous = current
                current = current.right
            
        if newvalue < previous.value:
            previous.left = Node(newvalue)
            previous.left.head = p.head
            return previous.left.head

        elif newvalue > previous.value:
            previous.right = Node(newvalue)
            previous.right.head = p.head
            return previous.right.head
    

def finns(p, value):
    if p is None:
        return False
    current = p

    while value <= current.value or value >= current.value:
        if value == current.value:
            return True
        if value <= current.value:
            current = current.left
            
            
        elif value >= current.value:
            current = current.right
        if current == None:
            return False


def skriv(p):
    if p == None:
        return

    skriv(p.left)
    print(p.value, end=' ')
    skriv(p.right)


if __name__ == "__main__":
    pass
    # q = Bintree()

    

    # q.put(50)
    # q.put(60)
    # q.put(30)
    # q.put(20)
    # q.put(40)
    # q.put(55)
    # q.put(70)
    
    # q.write()
    # #print(20 in q)
    # # q.put(45)
    # # q.put(55)
    # # q.put(70)