import sys
import numpy as np

def findSequence(lengthOfStrand, strand1, strand2):
    #numpy is used for its efficiency and ease of debugging
    dynamicTable = np.zeros((lengthOfStrand + 1, lengthOfStrand + 1), dtype = int)
    strTable = dynamicTable.astype(str)
    maxLength = 0
    longestCommonSubstring = ''
    matches = []
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
    for rows in strTable:
        matches += [strings for strings in rows if strings!='']
    matches = set(matches)  #remove copies
    matches = list(matches)
    return matches

#------testing
#x = findSequence(3 , "ABC", "ABD")
#y = findSequence(10, "AAAACCCTTG", "CCAAAACCTA")
#print(x)

#this is 100% my idea and I'm pretty proud of it.
#Funnily enough, first time I implemented this it was incorrect for high threshholds and I didn't notice
#until 30 minutes until the initial deadline, so the extension is greatly appreciated!

def processQueue(numberOfStrands, threshholdNumber, lengthOfStrand, queue):
    combinations = []
    for i in range(numberOfStrands - 1):
        for j in range(i, numberOfStrands - 1):
            #index is going to inform us on which strands we found the common sequence
            combinations.append([i, j + 1, findSequence(lengthOfStrand, queue[i], queue[j+1])])
    #now we have all the combinations of all the "longest substring" commands

    #This sorts the combinations according to length of the string (so longest string is checked first later)
    sortedCombinations = []
    for items in combinations:
        newItems = sorted(items[2], key = len)
        newItems.reverse()
        sortedCombinations.append([items[0], items[1],newItems])
    #starting with longest length possible, if no matches found, go to one length shorter.
    #If found string with desired length, add to dictionary
    for desiredLength in range(lengthOfStrand, 0, -1):
        dictionary = {}
        for triplets in sortedCombinations:
                items = triplets[2]
                for values in items:
                    if len(values) == desiredLength:
                        if values in dictionary:
                            temp = dictionary.get(values)
                            temp.append(triplets[0])
                            temp.append(triplets[1])
                            temp = set(temp) #removing copies - noting which strands the sequence appeared in
                            temp = list(temp)
                            dictionary[values] = temp
                        else:
                            dictionary[values] = [triplets[0], triplets[1]]
                    elif len(values) < desiredLength:
                        break
        #print(dictionary)
        # If there is an item in the dictionary, see if the number of occurences is higher or equal to desireds
        if len(dictionary) > 0:
            for keys in dictionary:
                if len(dictionary[keys]) >= threshholdNumber:
                    return dictionary
        #NOTE THAT IT RETURNS ONLY THE FIRST ONE FOUND. The specification of the assessment
        #clearly stated that the output should be just one string, not an array.

#-----------testing------------
#myQueue = ["ABC", "ABD", "BCD"]
#print(processQueue(3, 2, 3, myQueue))
#myQueue2 = ["AAAACCCTTG", "CCAAAACCTA"]
#print(processQueue(2, 2, 10, myQueue2))
#myQueue3 = ["AAAACCCTTG", "CCAAAACCTA", "ATCCATAACC"]
#print(processQueue(3, 2, 10, myQueue3))
#print(processQueue(3, 3, 10, myQueue3))
#myQueue4 = ["ATCGCGTAAATCACT",  "GGTCCAATATATCTT",  "TCGCGTACAACTACG",  "GAGAGATAATATACG", "TCGCTGATAGTCTAA", "AAGTAAAATGTAAAG"]
#print(myQueue4)
#print(processQueue(6, 3, 15, myQueue4))

def inputFunction():
    queue = []
    numberOfStrands, thresholdNumber, lengthOfStrand = sys.stdin.readline().split()
    numberOfStrands = int(numberOfStrands)
    thresholdNumber = int(thresholdNumber)
    lengthOfStrand = int(lengthOfStrand)

    for i in range(numberOfStrands):
        strand = sys.stdin.readline()
        queue.append(strand)
    longestSharedSequence = processQueue(numberOfStrands, thresholdNumber, lengthOfStrand, queue)
    print(longestSharedSequence)

inputFunction()
