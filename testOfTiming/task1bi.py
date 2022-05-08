import sys
#basic classes definition taken from https://www.geeksforgeeks.org/linked-list-set-1-introduction/ 
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
    def printListNice(self):
        temp = self.head
        nice = []
        while (temp):
            nice.append(temp.data)
            temp = temp.next
        print(''.join(nice))


#Function for putting the input into a linked list data structure
def createLinkedList(lengthOfStrand, strand, lengthOfSplicer, splicer, splicingIndex, lengthInsert, insert):
    
    linkedList = LinkedList()
    head = Node(strand[0])
    linkedList.head = head
    current = head
    for i in range(1,lengthOfStrand):
        current.next = Node(strand[i])
        current = current.next
    return linkedList

def insertIntoStrand(linkedList, lengthOfSplicer, splicer, splicingIndex, lengthInsert, insert):
    splicer = [characters for characters in splicer]
    current = linkedList.head
    backPointer = current
    checkSplicer = []

    while current != None:
        #print("back at the beginning")
        #linkedList.printListNice()
        temp = current.next     #remembering the next node in case an insertion happens
        checkSplicer.append(current.data)
        if len(checkSplicer) > lengthOfSplicer:
            checkSplicer.pop(0)
            #print("at if", backPointer.data)
            backPointer = backPointer.next
            #print("at if after assignment", backPointer.data)
        #print("after checkspplicer", current.data, checkSplicer, backPointer.data)
 
        if checkSplicer == splicer:

            current = backPointer
            splicerArray = splicer.copy()
            splicerArray.insert(splicingIndex, insert)
            splicerArray = ''.join(splicerArray)
            splicerArray = [characters for characters in splicerArray]
            splicerArray = splicerArray[1:]     #throwing out backPointer - otherwise it would double
            #print("Splicer found", splicerArray)
            checkSplicer = []    
            
            for i in range(len(splicerArray)):  
                current.next = Node(splicerArray[i])
                current = current.next 

                if i >= lengthInsert:            #setting up the check for chaining splitters
                    checkSplicer.append(current.data)

            current.next = temp
            current = current.next
            #print(current.next.next)
            for k in range(lengthInsert + 1):       #moving the back pointer past the inserted strand
                backPointer = backPointer.next
               #print("after adjusting", backPointer.data)
                
            
        else:
            current = current.next
    return linkedList
    linkedList.printListNice()
    #print("--")



    
    

#--------Testing------------

#newList = createLinkedList(16, "AATCCGAATTCGTATC", 6, "GAATTC", 1, 5, "TGATA")
#newList.printListNice()
#print("---")
#insertIntoStrand(newList, 6, "GAATTC", 1, 5, "TGATA")

#aList = createLinkedList(6, "AAAAAA", 3, "AAA", 1, 1, "T")
#insertIntoStrand(aList, 3, "AAA", 1, 1, "T")


#bList = createLinkedList(4, "CAAT", 1, "A", 1, 2, "GA")
#insertIntoStrand(bList, 1, "A", 1, 2, "GA")
#bList.printListNice()

#cList = createLinkedList(6, "ATXDAT", 2, "AT", 1, 3, "WOF")
#cList = insertIntoStrand(cList, 2, "AT", 1, 3, "WOF")
#cList.printListNice()








def inputFunction():
    result = None
    queue = []
    lengthOfStrand, numberOfOperations = sys.stdin.readline().split()
    lengthOfStrand = int(lengthOfStrand)
    numberOfOperations = int(numberOfOperations)
    strand = sys.stdin.readline()

    for i in range(numberOfOperations):
        lengthSplicer, lengthInsert, splicer, splicingIndex, insert = sys.stdin.readline().split()
        lengthSplicer = int(lengthSplicer)
        lengthInsert = int(lengthInsert)
        splicingIndex = int(splicingIndex)
        queue.append([lengthSplicer, splicer,splicingIndex, lengthInsert, insert])
    start = queue[0]
    list = createLinkedList(lengthOfStrand, strand, start[0], start[1],  start[2], start[3], start[4])
    for items in queue:
        list = insertIntoStrand(list, items[0], items[1], items[2], items[3], items[4])
    list.printListNice()


#inputFunction()