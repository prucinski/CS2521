from random import choice, randint
import time
import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#note how only the first longest sequence will be returned
def findSequence(lengthOfStrand, strand1, strand2):
    #numpy is used for its efficiency and ease of debugging
    dynamicTable = np.zeros((lengthOfStrand + 1, lengthOfStrand + 1), dtype = int)
    strTable = dynamicTable.astype(str)
    maxLength = 0
    longestCommonSubstring = ''
    for i in range(lengthOfStrand + 1):
        for j in range(lengthOfStrand + 1):
            if i == 0 or j == 0:        #skipping the first "convenience" row
                strTable[i][j] = ''
            elif strand1[i -1] == strand2[j-1]:     #compare characters - if match, add 1 to diagonal
                dynamicTable[i][j] = dynamicTable[i-1][j-1] + 1
                strTable[i][j] = strTable[i-1][j-1] + strand1[i-1]
                if dynamicTable[i][j] > maxLength:
                    maxLength = dynamicTable[i][j]
                    longestCommonSubstring = strTable[i][j]
            else:
                dynamicTable[i][j] = 0      #no match found
                strTable[i][j] = ''
    return longestCommonSubstring

#x = findSequence(3 , "ABC", "ABD")
#y = findSequence(10, "AAAACCCTTG", "CCAAAACCTA")
#print(y)

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
    print(strand1, strand2, longestCommonString)
    myTime = time.perf_counter() - myTime
    print(myTime, "s for running the algorythm")
    return myTime


def plotFunction():
    dnaLengths = [x for x in range(100,4000, 100)]
    print(len(dnaLengths))
    timeThis = []
    temp = []
    for dnaLength in dnaLengths:
        for i in range(20):
            temp.append(testFunction(dnaLength))
        timeThis.append(sum(temp)/len(temp))
        temp = []
    titleMessage = "Time of execution of algorythm 2b"
    plt.title(titleMessage)
    plt.plot(dnaLengths,timeThis, 'ro')
    plt.plot(dnaLengths,timeThis, 'r--')
    plt.ylabel('time to run (s)')
    plt.xlabel('Length of DNA strand')
    plt.minorticks_on()
    plt.grid(which = "major", alpha = 0.7)
    plt.grid(which = "minor", axis = "y", alpha = 0.2)
    #plt.savefig(('2b_'+".png"))
    plt.show()
    plt.clf()



#plotFunction()
