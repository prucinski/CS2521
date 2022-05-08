import sys
from random import choice, randint
import time

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def splice(lengthOfStrand, strand,  lengthSplicer,  splicer, splicingIndex, lengthInsert, insert):
    newStrand = []
    lastCheckableIndex = lengthOfStrand - lengthSplicer + 1
    i = 0
    while i != lastCheckableIndex:
        temp = strand[i:i+lengthSplicer]
        if temp == splicer:
            for j in range(splicingIndex):
                newStrand.append(strand[i+j])
            newStrand.append(insert)
            print(i)
            i+=j
        else:
            newStrand.append(strand[i])
        i+=1
    
    for i in range(lastCheckableIndex, lengthOfStrand):
        newStrand.append(strand[i])
    return "".join(newStrand)

#--------------tests---------------
#newSplice = splice(16, "AATCCGAATTCGTATC", 6, "GAATTC", 1, 5, "TGATA")
#twoSplice = splice(16, "AATCCGAATTCGTATC", 6, "GAATTC", 2, 5, "TTTTT")
#testSplice = splice(16, "AATCCGAATTCGTATC", 6, "AATCCG", 1, 5, "TGATA")
#aSplice = splice(6, "AAAAAA", 3, "AAA", 1, 1, "T")
#bSplice = splice(4, "CAAT", 1, "A", 1, 2, "GA")


#print(newSplice)
#print(twoSplice)
#print("AAAAAA\n",aSplice)
#print(bSplice)


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

    for items in queue:
        #print(lengthOfStrand, strand, items)
        strand = splice(lengthOfStrand, strand, items[0], items[1],  items[2], items[3], items[4])
        lengthOfStrand = len(strand)
        #print(strand)
    print(strand)


def testFunction(lengthOfStrand, lengthSplicer):
    print("generating string...")
    myTime = time.perf_counter()
    splicer = []
    strand = []
    allowed = "AGCT"
    #generating a random splicer
    for i in range(lengthSplicer): 
        splicer.append(choice(allowed))
    splicer = ''.join(splicer)

    #generating a random position where splicer will be inserted
    pos = randint(0, lengthOfStrand)
 
    #generating the strand with length of lengthOfStrand + lengthSplicer
    #and guaranteeing that random splicer will be inserted
    for i in range(lengthOfStrand):
        strand.append(choice(allowed))
    strand.append(splicer)
    for i in range(pos, lengthOfStrand):
        strand.append(choice(allowed))
    #print(time.perf_counter() - myTime, "s")
    strand = ''.join(strand)
    print(time.perf_counter() - myTime, "s for generation")
    print("String generated!")
    myTime = time.perf_counter()   
    strand = splice(lengthOfStrand, strand, lengthSplicer, splicer, 1, 10, "XXXXXXXXXX")
    myTime = time.perf_counter() - myTime
    print(myTime, "s for running the algorythm")
    
    return myTime


def plotFunction(insertLength):
    dnaLengths = [x for x in range(1000000,40000000, 4000000)]
    print(len(dnaLengths))
    timeThis = []
    temp = []
    for dnaLength in dnaLengths:
        for i in range(20):
            print("iteration", i, dnaLength)
            temp.append(testFunction(dnaLength, insertLength))
        timeThis.append(sum(temp)/len(temp))
        temp = []
    titleMessage = "Time of execution of algorythm 1a for insert length =" + str(insertLength)
    plt.title(titleMessage)
    plt.plot(dnaLengths,timeThis, 'ro')
    plt.plot(dnaLengths,timeThis, 'r--')
    plt.ylabel('time to run (s)')
    plt.xlabel('Length of DNA strand')
    plt.minorticks_on()
    plt.grid(which = "major", alpha = 0.7)
    plt.grid(which = "minor", axis = "y", alpha = 0.2)
    plt.savefig(('1a_NEW' +str(insertLength)+".png"))
    plt.clf()
    #plt.show()


inputFunction()
#plotFunction(10)
#plotFunction(100)
#plotFunction(1000)