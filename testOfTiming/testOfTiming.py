import task1bi
import task1bii
from random import choice, randint
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import time


def testFunctionBi(lengthOfStrand, lengthSplicer):
    print("generating string...")
    structureTime = time.perf_counter()
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
    print(time.perf_counter() - structureTime, "s for generation")
    print("String generated!")
    structureTime = time.perf_counter()   
    strandList = task1bi.createLinkedList(lengthOfStrand, strand, lengthSplicer, splicer, 1, 10, "AAAAAAAAAA")
    
    structureTime = time.perf_counter() - structureTime
    print(structureTime, "s for running the algorythm - load")
    insertTime = time.perf_counter()
    task1bi.insertIntoStrand(strandList,lengthSplicer, splicer, 1, 10, "AAAAAAAAAA")
    insertTime = time.perf_counter() - insertTime
    print(insertTime, "s for running the algorythm - insert")
    return [structureTime, insertTime]

def testFunctionBii(lengthOfStrand, lengthSplicer):
    print("generating string...")
    structureTime = time.perf_counter()
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
    print(time.perf_counter() - structureTime, "s for generation")
    print("String generated!")
    structureTime = time.perf_counter()   
    strandList = task1bii.createLinkedList(lengthOfStrand, strand, lengthSplicer, splicer, 1, 10, "AAAAAAAAAA")
    
    structureTime = time.perf_counter() - structureTime
    print(structureTime, "s for running the algorythm - load")
    insertTime = time.perf_counter()
    task1bii.insertIntoStrand(strandList,lengthSplicer, splicer, 1, 10, "AAAAAAAAAA")
    insertTime = time.perf_counter() - insertTime
    print(insertTime, "s for running the algorythm - insert")
    return [structureTime, insertTime]



def plotFunctionBi(insertLength):
    dnaLengths = [x for x in range(1000000,20000000, 2000000)]
    print(len(dnaLengths))
    timeThisStructure = []
    sumStructure = []
    timeThisInsert = []
    sumInsert = []
    temp = []
    for dnaLength in dnaLengths:
        for i in range(6):
            print("iteration", i, "for dnaLength ", dnaLength)
            temp.append(testFunctionBi(dnaLength, insertLength))
        for items in temp:
            sumStructure.append(items[0])
            sumInsert.append(items[1])
        timeThisStructure.append(sum(sumStructure)/len(temp))
        timeThisInsert.append(sum(sumInsert)/len(temp))
        sumStructure = []
        sumInsert = []
        temp = []
    titleMessage = "Time of execution of algorythm 1bi for loading into the structure, length =" + str(insertLength)
    plt.title(titleMessage)
    plt.plot(dnaLengths,timeThisStructure, 'ro')
    plt.plot(dnaLengths,timeThisStructure, 'r--')
    plt.ylabel('time to run (s)')
    plt.xlabel('Length of DNA strand')
    plt.minorticks_on()
    plt.grid(which = "major", alpha = 0.7)
    plt.grid(which = "minor", axis = "y", alpha = 0.2)
    plt.savefig(('1bi_load_NEW' +str(insertLength)+".png"))
    plt.clf()

    titleMessage = " Time of execution of algorythm 1bi for inserting the strand, length =" + str(insertLength)
    plt.title(titleMessage)
    plt.plot(dnaLengths,timeThisInsert, 'ro')
    plt.plot(dnaLengths,timeThisInsert, 'r--')
    plt.ylabel('time to run (s)')
    plt.xlabel('Length of DNA strand')
    plt.minorticks_on()
    plt.grid(which = "major", alpha = 0.7)
    plt.grid(which = "minor", axis = "y", alpha = 0.2)
    plt.savefig(('1bi_insert_NEW' +str(insertLength)+".png"))
    plt.clf()

def plotFunctionBii(insertLength):
    print('hello')
    dnaLengths = [x for x in range(1000000,20000000, 2000000)]
    print(len(dnaLengths))
    sumStructure = []
    timeThisInsert = []
    sumInsert = []
    timeThisStructure = []
    temp = []
    for dnaLength in dnaLengths:
        for i in range(6):
            print("iteration", i, "of length ", dnaLength)
            temp.append(testFunctionBii(dnaLength, insertLength))
        for items in temp:
            sumStructure.append(items[0])
            sumInsert.append(items[1])
        timeThisStructure.append(sum(sumStructure)/len(temp))
        timeThisInsert.append(sum(sumInsert)/len(temp))
        sumStructure = []
        sumInsert = []
        temp = []
    titleMessage = "Time of execution of algorythm 1bii for loading into the structure, length =" + str(insertLength)
    plt.title(titleMessage)
    plt.plot(dnaLengths,timeThisStructure, 'ro')
    plt.plot(dnaLengths,timeThisStructure, 'r--')
    plt.ylabel('time to run (s)')
    plt.xlabel('Length of DNA strand')
    plt.minorticks_on()
    plt.grid(which = "major", alpha = 0.7)
    plt.grid(which = "minor", axis = "y", alpha = 0.2)
    plt.savefig(('1bii_load_NEW' +str(insertLength)+".png"))  
    plt.clf()

    titleMessage = " Time of execution of algorythm 1bii for inserting the strand, length =" + str(insertLength)
    plt.title(titleMessage)
    plt.plot(dnaLengths,timeThisInsert, 'ro')
    plt.plot(dnaLengths,timeThisInsert, 'r--')
    plt.ylabel('time to run (s)')
    plt.xlabel('Length of DNA strand')
    plt.minorticks_on()
    plt.grid(which = "major", alpha = 0.7)
    plt.grid(which = "minor", axis = "y", alpha = 0.2)
    plt.savefig(('1bii_insert_NEW' +str(insertLength)+".png"))
    plt.clf()


plotFunctionBi(10)
#plotFunctionBi(100)
plotFunctionBi(1000)
#plotFunctionBii(10)
#plotFunctionBii(100)
#plotFunctionBii(1000)

print("Total time elapsed: ", time.perf_counter())

#py C:\Users\agent\Desktop\CS2521\testOfTiming\testOfTiming.py