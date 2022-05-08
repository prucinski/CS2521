import sys
from random import choice, randint
import time
import gc
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#from functools import lru_cache

def findSubstrings(string, lengthOfSubstring):
    substringList = []
    for i in range (len(string) - lengthOfSubstring + 1):
        substringList.append(string[i:lengthOfSubstring+i])
    return substringList

sys.setrecursionlimit(3000)
#@lru_cache(100)
def findSequence(lengthOfStrand, strand1, strand2, passToNext = 0):
    
    lengthOfSubstring = lengthOfStrand - passToNext
    if lengthOfSubstring == 0:
        return ""
    substrings1 = set(findSubstrings(strand1, lengthOfSubstring))    #argument substringList =[] needs to be given because for whatever reason it returns substringList to global memory
    substrings2 = set(findSubstrings(strand2, lengthOfSubstring))    #my guess its due to the fact that when defining arrays using other arrays, they are defined by reference, not by value
    commonSet = substrings1 & substrings2                                               #thus it gets the reference to the array that was initially (at the beginning of the programme) an empty array
    if len(commonSet) > 0:
        return commonSet.pop()
    return findSequence(lengthOfStrand, strand1, strand2, passToNext+1)




#print(findSubstrings("ABCDEF", 3))
#print(findSequence(10, "AAAACCCTTG", "CCAAAACCTA"))
#print(findSequence(6, "AAAACC", "GGGGTT"))




def inputFunction():
    queue = []
    numberOfStrands, thresholdNumber, lengthOfStrand = sys.stdin.readline().split()
    numberOfStrands = int(numberOfStrands)
    thresholdNumber = int(thresholdNumber)
    lengthOfStrand = int(lengthOfStrand)

    for i in range(numberOfStrands):
        strand = sys.stdin.readline()
        queue.append(strand)
    longestSharedSequence = findSequence(lengthOfStrand, queue[0], queue[1])
    print(longestSharedSequence)

inputFunction()



def testFunction(lengthOfStrand):
    print("generating strings...")
    myTime = time.perf_counter()
    strand1 = []
    strand2 = []
    allowed = "AGCT"
    #generating the strand with length of lengthOfStrand 
    for i in range(lengthOfStrand):
        strand1.append(choice(allowed))
        strand2.append(choice(allowed))
    strand1 = ''.join(strand1)
    strand2 = ''.join(strand2)

    print(time.perf_counter() - myTime, "s for generation")

    myTime = time.perf_counter()   
    longestCommonString = findSequence(lengthOfStrand, strand1, strand2)
    #print(strand1, strand2, longestCommonString)
    myTime = time.perf_counter() - myTime
    print(myTime, "s for running the algorythm")
    return myTime


def plotFunction():
    #2200 is as far as its going to go without crashing
    dnaLengths = [x for x in range(100,2200, 100)]
    print(len(dnaLengths))
    timeThis = []
    temp = []
    for dnaLength in dnaLengths:
        for i in range(20):
            temp.append(testFunction(dnaLength))
        timeThis.append(sum(temp)/len(temp))
        temp = []
    titleMessage = "Time of execution of algorythm 2a"
    plt.title(titleMessage)
    plt.plot(dnaLengths,timeThis, 'ro')
    plt.plot(dnaLengths,timeThis, 'r--')
    plt.ylabel('time to run (s)')
    plt.xlabel('Length of DNA strand')
    plt.minorticks_on()
    plt.grid(which = "major", alpha = 0.7)
    plt.grid(which = "minor", axis = "y", alpha = 0.2)
    plt.savefig(('2a_n'+".png"))
    plt.show()
    plt.clf()



#plotFunction()