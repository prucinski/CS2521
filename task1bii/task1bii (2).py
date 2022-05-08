
import sys
import math
#basic classes definition taken from https://www.geeksforgeeks.org/linked-list-set-1-introduction/ 
class Node():
    def __init__(self, data, hash = None):
        self.data = data
        self.hash = hash
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
    def printHashes(self):
        temp = self.head
        while(temp):
            print(temp.hash)
            temp = temp.next
    def printListNice(self):
        temp = self.head
        nice = []
        while (temp):
            nice.append(temp.data)
            temp = temp.next
        print(''.join(nice))

#this is just for the string with the splicer 
def calculateHashFirst(splicer):
    hash = 0
    alphabetLength = 4
    primeModulus = 101
    i=0
    for characters in splicer:
        if characters == "A":
            thisHash = 1
        elif characters == "T":
            thisHash = 2
        elif characters == "C":
            thisHash = 3
        elif characters == "G":
            thisHash = 4
        hash = hash +  math.pow(alphabetLength, len(splicer)-i-1)*thisHash
    return hash


#Function for putting the input into a linked list data structure
def createLinkedList(lengthOfStrand, strand, lengthOfSplicer, splicer, splicingIndex, lengthInsert, insert):

    #each node holds the hash of values for lengthOfSplicer previous nodes. This is to retrofit the implementation from 1bi
    def calculateHash(previousHash, node):
        alphabetLength = 4
        primeModulus = 101
        if node.data == "A":
            thisHash = 1
        elif node.data == "T":
            thisHash = 2
        elif node.data == "C":
            thisHash = 3
        elif node.data == "G":
            thisHash = 4
        hash = ((previousHash + primeModulus - thisHash*((alphabetLength%primeModulus)*alphabetLength)%primeModulus)*alphabetLength * thisHash)%primeModulus
        return hash
    
    linkedList = LinkedList()
    head = Node(strand[0:lengthOfSplicer])
    head.hash = calculateHashFirst(head.data)
    linkedList.head = head
    current = head
    for i in range(lengthOfSplicer,lengthOfStrand):
        current.next = Node(strand[i])
        current.next.hash = calculateHash(current.hash, current.next)
        current = current.next
    return linkedList

def insertIntoStrand(linkedList, lengthOfSplicer, splicer, splicingIndex, lengthInsert, insert):

    #This is spaghetti code - I am defining the same function twice within different functions because I don't want to have "lengthOfSplicer" in the function call
    #Defining it in main would have to have this definition: calculateHash(previousHash, node, lengthOfSplicer) and its too long for my liking
    def calculateHash(previousHash, node):
        alphabetLength = 4
        primeModulus = 101
        if node.data == "A":
            thisHash = 1
        elif node.data == "T":
            thisHash = 2
        elif node.data == "C":
            thisHash = 3
        elif node.data == "G":
            thisHash = 4
        hash = ((previousHash + primeModulus - thisHash*((alphabetLength%primeModulus)*alphabetLength)%primeModulus)*alphabetLength * thisHash)%primeModulus
        return hash

    splicer = [characters for characters in splicer]
    splicerHash = calculateHashFirst(splicer)
    current = linkedList.head
    backPointer = current
    moveNextIter = 0
    while current != None:
        #print("back at the beginning")
        #linkedList.printListNice()
        temp = current.next     #remembering the next node in case an insertion happens

        #if hash is the desired length, move backpointer forward on next iteration
        #if hash has length 1, move backpointer this iteration
        if current.hash > math.pow(10, lengthOfSplicer - 1):
            if moveNextIter== 0 and lengthOfSplicer !=1:
                moveNextIter = 1
            else:
                backPointer = backPointer.next

 
        if current.hash == splicerHash:

            current = backPointer
            splicerArray = splicer.copy()
            splicerArray.insert(splicingIndex, insert)
            splicerArray = ''.join(splicerArray)
            splicerArray = [characters for characters in splicerArray]
            splicerArray = splicerArray[1:]     #throwing out backPointer - otherwise it would double
          
            for i in range(len(splicerArray)):  
                current.next = Node(splicerArray[i])
                current.next.hash = calculateHash(current.hash, current.next)
                current = current.next 

                if i >= lengthInsert:            #setting up the check for chaining splitters
                   moveNextIter = 0

            current.next = temp
            if current.next != None:
                current.next.hash = calculateHash(current.hash, current.next)
            current = current.next

            for k in range(lengthInsert + 1):       #moving the back pointer past the inserted strand
                backPointer = backPointer.next
               #print("after adjusting", backPointer.data)
                
            
        else:
            current = current.next
    return linkedList
    




#--------Testing------------
print(calculateHashFirst("ACG"))
newList = createLinkedList(16, "AATCCGAATTCGTATC", 6, "GAATTC", 1, 5, "TGATA")
#print(calculateHashFirst("GAATTC"))
#print(calculateHashFirst("AATCCG"))
#print(calculateHashFirst("ATCCGA"))
print("---")
newList.printHashes()
#print("---")
newList.printListNice()
insertIntoStrand(newList, 6, "GAATTC", 1, 5, "TGATA")
newList.printListNice()

aList = createLinkedList(6, "AAAAAA", 3, "AAA", 1, 1, "T")
#aList.printHashes()
aList.printListNice()
insertIntoStrand(aList, 3, "AAA", 1, 1, "T")
aList.printListNice()


bList = createLinkedList(4, "CAAT", 1, "A", 1, 2, "GA")
#bList.printHashes()
bList.printListNice()
insertIntoStrand(bList, 1, "A", 1, 2, "GA")
bList.printListNice()

cList = createLinkedList(6, "ATCTAT", 2, "AT", 1, 3, "GTC")
cList.printListNice()
cList = insertIntoStrand(cList, 2, "AT", 1, 3, "GTC")
cList.printListNice()








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