# Name: Kyle Fritz
# File: main.py
# Date Created: 10/11/16
# Description: Algorithms Project 1, 
# Usage: python main.py file.txt 
#  or use ./run after initiating run

import sys # for getting input file

def OPT():
	return

# Takes in a list, finds the indexes of the first appearance of 'G', 'H', 'T', 'W'
def getIndexes(peopleList):
	if 'G' and 'H' and 'T' and 'W' not in peopleList:
		return 0, 0, 0, 0	
	else:
		indG = 0
		for i in range(1, len(peopleList)): # 0 has been checked, so start at 1
			if peopleList[i] == 'H':
				indH = i
				break # next
		for i in range(indH + 1, len(peopleList)): # indH has already been looked at, so start at indH + 1
			if peopleList[i] == 'T':
                                indT = i
                                break # next
		for i in range(indT + 1, len(peopleList)):
                        if peopleList[i] == 'W':
                                indW = i
                                break # next
		return indG, indH, indT, indW

def main():
	filename = sys.argv[-1] # The file name given
	openedFile = open(filename) # the file is opened

	peopleList = list(openedFile.read()) # Get a list of all the types of people
	peopleList.pop() # pop off the '\n'
	peopleList.sort() # Sorts the list in alphabetic order {G, H, T, W}
	peopleLen = len(peopleList) # Number of people
	indG, indH, indT, indW = getIndexes(peopleList)
	print(indG, indT)
	print(peopleLen)
	print(peopleList)
	return
main()
