class LinkedQ:
    def __init__(self):
        self.__head = None # skapar huvudet på kön None.

    def isEmpty(self):
        return self.__head == None # kollar om kön är tom

    def enqueue(self, item):
        temp = Node(item) # Skapar ett nod objekt med ett värde och värdet på nästa nod
        temp.setNext(self.__head) # Lägg till hela köns "historia" till temp
        self.__head = temp # koppla ihop nya noden med head.

    def dequeue(self):
        previous = None 
        current = self.__head # sätter två flaggor som vi rör frammåt i kön genom while loopen tills vi hitter den första i kön
        
        while current.getNext() != None: 
            previous = current # flytta fram föregående nod till nästa nod
            current = current.getNext() # flytta fram noden ett steg i kön

        if previous == None:    # kollar om vi flyttat fram något steg över huvudtaget, 
            self.__head = None  # om inte ( finns bara ett eller noll noder i kön) sätter vi kön till tom genom None
            pass
        else:
            previous.setNext(None)  # kopplar samman det näst första (nya första) med None, dvs längst fram. (första noden pekar inte på någon annan nod utan till jord)
        return current.getData()    # Skickar tillbaka värdet på noden som står längst fram i kön

            
        

    def size(self):
        current = self.__head
        count = 0
        while current != None:  # gör en loop tills vi kommer längst frak i kön
            count += 1
            current.getNext()
        return count            # returnerar hur lång kön blev




class Node:
    def __init__(self,initdata):    # när en ny nod skapas ansätter man dess värde men kopplar den inte direkt till nästa nod.
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):      # kanske är en onödig funktion för vårat usecase. fanns med i dokumentationen och kan vara användbar om man skulle vilja byta värdet på något i kön
        self.data = newdata

    def setNext(self,newnext):      # Här ansätts kopplingen till nästa nod...
        self.next = newnext



if __name__ == "__main__":          # test script för metoden. har använts för att hitta buggar... användbart har varit att sätta input() för att kontrollera o se vad som händer.
    kort = input().split()
    q = LinkedQ()
    for i in kort:
        q.enqueue(int(i))

    while not q.isEmpty():
        q.enqueue(q.dequeue())
        x = q.dequeue()
        print(x)
        