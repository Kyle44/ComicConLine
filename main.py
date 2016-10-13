# Name: Kyle Fritz
# File: main.py
# Date Created: 10/11/16
# Description: Algorithms Project 1, 
# Usage: python main.py file.txt 
#  or use ./run after initiating run

import sys # for getting input file

def OPT():
	return

def main():
	filename = sys.argv[-1] # The file name given
	openedFile = open(filename) # the file is opened

	peopleList = list(openedFile.read()) # Get a list of all the types of people
	peopleList.pop() # pop off the '\n'
	print(peopleList)
	return
main()
