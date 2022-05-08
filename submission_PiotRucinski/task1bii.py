
import sys
import math
#basic classes definition taken from my code from CS1527 course practicals
#which in turn were inspired by https://www.geeksforgeeks.org/linked-list-set-1-introduction/
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
    def returnList(self):
        temp = self.head
        list = []
        while (temp):
            list.append(temp.data)
            temp = temp.next
        return ''.join(list)

#this is just for the string with the splicer. Each hash is unique.
def calculateHashFirst(splicer):
    hash = 0
    alphabetLength = 4
    i = 0
    primeNumber = 997
    for characters in splicer:
        if characters == "A":
            thisHash = 1
        elif characters == "T":
            thisHash = 2
        elif characters == "C":
            thisHash = 3
        elif characters == "G":
            thisHash = 4
        hash = int(hash +  math.pow(alphabetLength, len(splicer)-i-1)*thisHash)
        i+=1
    hash = hash%primeNumber
    return hash


#Function for putting the input into a linked list data structure
def createLinkedList(lengthOfStrand, strand, lengthOfSplicer, splicer, splicingIndex, lengthInsert, insert):

    #each node holds the hash of values for lengthOfSplicer previous nodes. This is to retrofit the implementation from 1bi
    def calculateHash(previousHash, node, backPointer):
        alphabetLength = 4
        constant = int(math.pow(alphabetLength,lengthOfSplicer - 1))
        primeNumber = 997
        if node.data == "A":
            thisHash = 1
        elif node.data == "T":
            thisHash = 2
        elif node.data == "C":
            thisHash = 3
        elif node.data == "G":
            thisHash = 4
        if backPointer.data == "A":
            prevFirstHash = 1
        elif backPointer.data == "T":
            prevFirstHash = 2
        elif backPointer.data == "C":
            prevFirstHash = 3
        elif backPointer.data == "G":
            prevFirstHash = 4
        hash = alphabetLength*(previousHash - constant*prevFirstHash) + thisHash
        hash = hash%primeNumber
        return hash
    
    linkedList = LinkedList()
    head = Node(strand[0])
    head.hash = -1
    linkedList.head = head
    backPointer = head
    current = head
    for i in range(1, lengthOfStrand):
        current.next = Node(strand[i])
        if i < lengthOfSplicer - 1:
            current.next.hash = -1
        elif i == lengthOfSplicer - 1:
            current.next.hash = calculateHashFirst(strand[0:i+1])
        elif lengthOfSplicer == 1:
            current.next.hash = calculateHashFirst(strand[i])
        else:
            current.next.hash = calculateHash(current.hash, current.next, backPointer)
            backPointer = backPointer.next
        current = current.next
    return linkedList



def insertIntoStrand(linkedList, lengthOfSplicer, splicer, splicingIndex, lengthInsert, insert):

    #This is spaghetti code - I am defining the same function twice within different functions because I don't want to have "lengthOfSplicer" in the function call
    #Defining it in main would have to have this definition: calculateHash(previousHash, node, lengthOfSplicer) and its too long for my liking
    def calculateHash(previousHash, node, backPointer):
        alphabetLength = 4
        primeNumber = 997
        constant = int(math.pow(alphabetLength,lengthOfSplicer - 1))
        if node.data == "A":
            thisHash = 1
        elif node.data == "T":
            thisHash = 2
        elif node.data == "C":
            thisHash = 3
        elif node.data == "G":
            thisHash = 4
        if backPointer.data == "A":
            prevFirstHash = 1
        elif backPointer.data == "T":
            prevFirstHash = 2
        elif backPointer.data == "C":
            prevFirstHash = 3
        elif backPointer.data == "G":
            prevFirstHash = 4
        hash = alphabetLength*(previousHash - constant*prevFirstHash) + thisHash
        hash = hash%primeNumber
        return hash
    

    splicer = [characters for characters in splicer]
    splicerHash = calculateHashFirst(splicer)
    #print(splicerHash)
    current = linkedList.head
    backPointer = current
    moveNextIter = 0
    while current != None:
        #print("back at the beginning")
        #linkedList.printListNice()
        temp = current.next     #remembering the next node in case an insertion happens

        #if hash is the desired length, move backpointer forward on next iteration
        #if hash has length 1, move backpointer this iteration
        if current.hash > 0:
            if moveNextIter== 0 and lengthOfSplicer !=1:
                moveNextIter = 1
            else:
                backPointer = backPointer.next

 
        if current.hash == splicerHash:
            word = []
            tempBuilder = backPointer
            i = 0
            while tempBuilder != current.next:       #hash found, check if the strings match
                word += tempBuilder.data
                tempBuilder = tempBuilder.next
                if word[i] != splicer[i]:
                    break
                i+=1
            if word == splicer: 
                current = backPointer
                splicerArray = splicer.copy()
                splicerArray.insert(splicingIndex, insert)
                splicerArray = ''.join(splicerArray)
                splicerArray = [characters for characters in splicerArray]
                splicerArray = splicerArray[1:]     #throwing out backPointer - otherwise it would double
          
                for i in range(len(splicerArray)):  
                    current.next = Node(splicerArray[i])    
                    current.next.hash = -1          #No rehashing is done - this is because the hash is dependent on the length
                                                    #of the string we are seeking for. The structure has to be generated again.
                    current = current.next 

                    #if i >= lengthInsert:            #setting up the check for chaining splitters
                    #   moveNextIter = 0

                current.next = temp
                #if current.next != None:
                    #current.next.hash = calculateHash(current.hash, current.next, backPointer)
                    #print(current.next.hash)
                current = current.next

                for k in range(lengthInsert):       #moving the back pointer past the inserted strand
                    backPointer = backPointer.next
                   #print("after adjusting", backPointer.data)
            else:
               current=current.next
        else:
            current = current.next
    return linkedList
    




#--------Testing------------
#print(calculateHashFirst("ACG"))
#print(calculateHashFirst("GAATTC"))
#print(calculateHashFirst("AATCCG"))
#print(calculateHashFirst("ATCCGA"))
#print(calculateHashFirst("TCCGAA"))
#print(calculateHashFirst("CCGAAT"))
#print(calculateHashFirst('CGTATC'))
#print(calculateHashFirst('AATTCG'))

#print("---")
#newList = createLinkedList(16, "AATCCGAATTCGTATC", 6, "GAATTC", 1, 5, "TGATA")

#newList.printHashes()
#print("---")
#newList.printListNice()


#insertIntoStrand(newList, 6, "GAATTC", 1, 5, "TGATA")
#newList.printListNice()
#a = input("")

#aList = createLinkedList(6, "AAAAAA", 3, "AAA", 1, 1, "T")
#aList.printHashes()
#aList.printListNice()
#insertIntoStrand(aList, 3, "AAA", 1, 1, "T")
#aList.printListNice()


#bList = createLinkedList(4, "CAAT", 1, "A", 1, 2, "GA")
#bList.printListNice()
#bList.printHashes()
#insertIntoStrand(bList, 1, "A", 1, 2, "GA")
#bList.printListNice()

#cList = createLinkedList(6, "ATCTAT", 2, "AT", 1, 3, "GTC")
#cList.printListNice()
#cList = insertIntoStrand(cList, 2, "AT", 1, 3, "GTC")
#cList.printListNice()



def inputFunction():
    flag = 0
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
        if flag:
            convList = list.returnList()
            list = createLinkedList(len(convList), convList, items[0], items[1], items[2],items[3], items[4])
        list = insertIntoStrand(list, items[0], items[1], items[2], items[3], items[4])
        flag = 1
    list.printListNice()

inputFunction()